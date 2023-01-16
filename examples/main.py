import sys
sys.path.insert(1, '../')

from conductor.client.workflow.conductor_workflow import ConductorWorkflow
from conductor.client.workflow.executor.workflow_executor import WorkflowExecutor
from conductor.client.workflow.task.simple_task import SimpleTask
from conductor.client.workflow.task.switch_task import SwitchTask
from conductor.client.workflow.task.task import TaskInterface
from examples.api import api_util
from examples.worker import worker_util
from examples.workflow import workflow_util
from examples.workflow.workflow_input import NotificationPreference
from examples.workflow.workflow_input import WorkflowInput


def create_email_or_sms_task() -> TaskInterface:
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
    workflow.add(
        SimpleTask('get_user_info', 'get_user_info').input(
            'userId', '${workflow.input.userId}')
    )
    workflow >> create_email_or_sms_task()

    workflow.register(overwrite=True)

    workflow_input = WorkflowInput('userA')
    workflow_util.start_workflow_sync(
        workflow_executor, workflow, workflow_input
    )
    workflow_util.start_workflow_async(
        workflow, workflow_input
    )

    task_handler.stop_processes()


if __name__ == '__main__':
    main()
