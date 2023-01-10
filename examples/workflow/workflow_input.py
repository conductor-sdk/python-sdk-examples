from enum import Enum


class NotificationPreference(str, Enum):
    EMAIL = 'EMAIL'
    SMS = 'SMS'


class WorkflowInput:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.notification_pref = NotificationPreference.EMAIL
