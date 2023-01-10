from conductor.client.automator.task_handler import TaskHandler
from conductor.client.worker.worker import Worker
from conductor.client.worker.worker_interface import WorkerInterface

from examples.api import api_util
from examples.worker import workers


def start_workers() -> TaskHandler:
    task_handler = TaskHandler(
        workers=[
            create_worker_get_user_info(),
            create_worker_send_email(),
            create_worker_send_sms()
        ],
        configuration=api_util.get_configuration()
    )
    task_handler.start_processes()
    print('started all workers')
    return task_handler


def create_worker_get_user_info() -> WorkerInterface:
    return Worker(
        task_definition_name='get_user_info',
        execute_function=workers.get_user_info,
        poll_interval=0.5
    )


def create_worker_send_email() -> WorkerInterface:
    return Worker(
        task_definition_name='send_email',
        execute_function=workers.send_email,
        poll_interval=0.5
    )


def create_worker_send_sms() -> WorkerInterface:
    return Worker(
        task_definition_name='send_sms',
        execute_function=workers.send_sms,
        poll_interval=0.5
    )
