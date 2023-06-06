from conductor.client.automator.task_handler import TaskHandler
from examples.api import api_util


def start_workers() -> TaskHandler:
    task_handler = TaskHandler(
        workers=[],
        configuration=api_util.get_configuration(),
        scan_for_annotated_workers=True
    )
    task_handler.start_processes()
    print('started all workers')
    return task_handler
