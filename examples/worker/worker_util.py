from conductor.client.automator.task_handler import TaskHandler
from conductor.client.http.models.task import Task
from conductor.client.http.models.task_result import TaskResult
from conductor.client.worker.worker import Worker
from conductor.client.worker.worker_interface import WorkerInterface

from examples.api.api_util import get_configuration
from examples.worker.workers import get_user_info
from examples.worker.workers import send_email
from examples.worker.workers import send_sms


def start_workers() -> TaskHandler:
    task_handler = TaskHandler(
        workers=[
            create_worker_get_user_info(),
            create_worker_send_email(),
            create_worker_send_sms()
        ],
        configuration=get_configuration()
    )
    task_handler.start_processes()
    print('started all workers')
    return task_handler


def create_worker_get_user_info() -> WorkerInterface:
    return Worker(
        task_definition_name='get_user_info',
        execute_function=get_user_info,
        poll_interval=0.5
    )


def create_worker_send_email() -> WorkerInterface:
    return Worker(
        task_definition_name='send_email',
        execute_function=send_email,
        poll_interval=0.5
    )


def create_worker_send_sms() -> WorkerInterface:
    return Worker(
        task_definition_name='send_sms',
        execute_function=send_sms,
        poll_interval=0.5
    )
