from conductor.client.http.models.start_workflow_request import StartWorkflowRequest

from examples.api import api_util
from examples.workflow import workflow_creator
from examples.workflow.workflow_input import WorkflowInput

import time


def start_workflow_sync():
    pass


def start_workflow_async():
    workflow = workflow_creator.create_complex_workflow()
    print(workflow.to_workflow_def())
    workflow.register(overwrite=True)

    workflow_input = WorkflowInput('userA')

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

    time.sleep(7)

    print()
    print('=======================================================================================')
    print("Workflow Execution Completed")
    print(f"Workflow Id: {workflow_id}")
    print(
        f"Workflow Execution Flow UI: {api_util.get_workflow_execution_url(workflow_id)}")
    print('=======================================================================================')
