import sys
sys.path.insert(1, '../')

from examples.worker import worker_util
from examples.workflow import workflow_util

task_handler = worker_util.start_workers()
workflow_util.start_workflow_sync()
workflow_util.start_workflow_async()
task_handler.stop_processes()
