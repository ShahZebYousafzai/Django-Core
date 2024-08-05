
import os
from .misc import yaml_coerce


def get_settings_from_environment(prefix):
    if not isinstance(prefix, str):
        raise TypeError(f"Expected 'prefix' to be a string, got {type(prefix).__name__}")

    prefix_len = len(prefix)
    settings = {}
    for key, value in os.environ.items():
        if key.startswith(prefix):
            stripped_key = key[prefix_len:]
            settings[stripped_key] = yaml_coerce(value)
    return settings
