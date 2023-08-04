from conductor.client.http.models.task import Task
from conductor.client.http.models.task_result import TaskResult
from conductor.client.http.models.task_exec_log import TaskExecLog
from conductor.client.http.models.task_result_status import TaskResultStatus

from examples.worker.user_info import UserInfo

import socket


def fraud_check(task: Task) -> UserInfo:
    userId = task.input_data['userId']
    return UserInfo(name='User X', id=userId)


def send_email(task: Task) -> TaskResult:
    email = task.input_data['email']
    task_result = get_task_result_from_task(task)
    task_result.logs.append(
        TaskExecLog(
            log=f'sent email to: {email}'
        )
    )
    task_result.status = TaskResultStatus.COMPLETED
    return task_result


def send_sms(task: Task) -> TaskResult:
    phoneNumber = task.input_data['phoneNumber']
    task_result = get_task_result_from_task(task)
    task_result.logs.append(
        TaskExecLog(
            log=f'sent sms to: {phoneNumber}'
        )
    )
    task_result.status = TaskResultStatus.COMPLETED
    return task_result


def get_task_result_from_task(task: Task) -> TaskResult:
    return TaskResult(
        task_id=task.task_id,
        workflow_instance_id=task.workflow_instance_id,
        worker_id=socket.gethostname(),
        logs=[],
    )
