import sys
sys.path.insert(1, '../')

from conductor.client.workflow.executor.workflow_executor import WorkflowExecutor
from conductor.client.workflow.conductor_workflow import ConductorWorkflow
from examples.api import api_util
from examples.worker import worker_util
from examples.workflow import workflow_util
from examples.workflow import workflow_creator


def create_complex_workflow() -> ConductorWorkflow:
    workflow_executor = WorkflowExecutor(api_util.get_configuration())
    workflow = ConductorWorkflow(
        executor=workflow_executor,
        name='user_notification',
        version=1,
    ).input_parameters(
        ['userId', 'notificationPref']
    ).add(
        workflow_creator.create_get_user_details_task()
    )
    workflow >> workflow_creator.create_email_or_sms_task()
    return workflow


task_handler = worker_util.start_workers()

workflow = create_complex_workflow()
workflow.register(overwrite=True)

workflow_util.start_workflow_sync(workflow)
workflow_util.start_workflow_async(workflow)

task_handler.stop_processes()
