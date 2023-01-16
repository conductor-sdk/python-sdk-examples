from conductor.client.http.models.start_workflow_request import StartWorkflowRequest
from conductor.client.workflow.conductor_workflow import ConductorWorkflow
from conductor.client.workflow.executor.workflow_executor import WorkflowExecutor
from examples.api import api_util
import time
import uuid


def start_workflow_sync(workflow_executor: WorkflowExecutor, workflow: ConductorWorkflow, workflow_input) -> None:
    workflow_run = workflow_executor.workflow_client.execute_workflow(
        body=StartWorkflowRequest(workflow.name),
        request_id=str(uuid.uuid4()),
        name=workflow.name,
        version=workflow.version,
        wait_until_task_ref='',
    )
    execution_url = api_util.get_workflow_execution_url(
        workflow_run.workflow_id
    )
    print()
    print('=======================================================================================')
    print('Workflow Execution Completed')
    print(f'Workflow Id: {workflow_run.workflow_id}')
    print(f'Workflow Status: {workflow_run.status}')
    print(f'Workflow Output: {str(workflow_run.output)}')
    print(f'Workflow Execution Flow UI: {execution_url}')
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
