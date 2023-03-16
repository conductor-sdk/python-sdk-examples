import sys
sys.path.insert(1, '../')

from conductor.client.http.models.start_workflow_request import StartWorkflowRequest
from conductor.client.workflow.conductor_workflow import ConductorWorkflow
from conductor.client.workflow.executor.workflow_executor import WorkflowExecutor
from conductor.client.workflow.task.simple_task import SimpleTask
from conductor.client.workflow.task.switch_task import SwitchTask
from conductor.client.workflow.task.task import TaskInterface
from examples.api import api_util
from examples.worker import worker_util
from examples.workflow.workflow_input import NotificationPreference
from examples.workflow.workflow_input import WorkflowInput
import logging
import time

logging.disable(level=logging.DEBUG)


def decision_task() -> TaskInterface:
    task = SwitchTask('emailorsms', '${workflow.input.notificationPref}')
    task.switch_case(
        NotificationPreference.EMAIL,
        SimpleTask('send_email', 'send_email').input(
            'email', '${get_user_info.output.email}')
    )
    task.switch_case(
        NotificationPreference.SMS,
        SimpleTask('send_sms', 'send_sms').input(
            'phoneNumber', '${get_user_info.output.phoneNumber}')
    )
    return task


def main():
    task_handler = worker_util.start_workers()

    workflow_executor = WorkflowExecutor(api_util.get_configuration())

    workflow = ConductorWorkflow(
        executor=workflow_executor,
        name='user_notification',
        version=1,
    )
    workflow.input_parameters = ['userId', 'notificationPref']
    simple_task = SimpleTask('get_user_info', 'get_user_info').input(
        'userId', '${workflow.input.userId}')

    workflow.add(simple_task)
    workflow >> decision_task()  # you can also use >> operator

    workflow.register(overwrite=True)  # register the workflow with the server

    workflow_input = WorkflowInput('userA')

    # Execute workflow synchronously, the call will wait until the workflow completes
    start_workflow_sync(workflow_executor, workflow, workflow_input)

    # Start async execution, returns the id of the workflow
    start_workflow_async(workflow, workflow_input)

    task_handler.stop_processes()


def start_workflow_sync(workflow_executor: WorkflowExecutor, workflow: ConductorWorkflow, workflow_input) -> None:
    workflow_run = workflow_executor.execute_workflow(
        request=StartWorkflowRequest(
            name=workflow.name,
            version=workflow.version
        ),
        wait_until_task_ref='',
    )
    print()
    print('=======================================================================================')
    print('Workflow Execution Completed')
    print(f'Workflow Id: {workflow_run.workflow_id}')
    print(f'Workflow Status: {workflow_run.status}')
    print(f'Workflow Output: {str(workflow_run.output)}')
    print(
        f'Workflow Execution Flow UI: {api_util.get_workflow_execution_url(workflow_run.workflow_id)}')
    print('=======================================================================================')


def start_workflow_async(workflow: ConductorWorkflow, workflow_input) -> None:
    workflow_id = workflow.start_workflow(
        StartWorkflowRequest(
            name=workflow.name,
            version=workflow.version,
            input={
                'userId': workflow_input.user_id,
                'notificationPref': workflow_input.notification_pref
            }
        )
    )
    execution_url = api_util.get_workflow_execution_url(workflow_id)
    time.sleep(4)
    print()
    print('=======================================================================================')
    print('Workflow Execution Completed')
    print(f'Workflow Id: {workflow_id}')
    print(f'Workflow Execution Flow UI: {execution_url}')
    print('=======================================================================================')


if __name__ == '__main__':
    main()
