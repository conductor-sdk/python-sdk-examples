import sys
sys.path.insert(1, '../')

from examples.worker.worker_util import start_workers

task_handler = start_workers()
task_handler.stop_processes()
