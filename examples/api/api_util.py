from conductor.client.configuration.configuration import Configuration
from conductor.client.configuration.settings.authentication_settings import AuthenticationSettings
from typing import Dict
import os

KEY = 'KEY'
SECRET = 'SECRET'
CONDUCTOR_SERVER_URL = 'CONDUCTOR_SERVER_URL'


def get_configuration():
    envs = _get_environment_variables()
    params = {
        'server_api_url': envs[CONDUCTOR_SERVER_URL],
        'debug': True,
        'authentication_settings': AuthenticationSettings(
            key_id=envs[KEY],
            key_secret=envs[SECRET]
        )
    }
    return Configuration(**params)


def _get_environment_variables() -> Dict[str, str]:
    envs = {
        KEY: '',
        SECRET: '',
        CONDUCTOR_SERVER_URL: ''
    }
    for env_key in envs.keys():
        value = os.getenv(env_key)
        if value is None or value == '':
            raise RuntimeError(f'environment variable not set: {env_key}')
        envs[env_key] = value
    return envs
