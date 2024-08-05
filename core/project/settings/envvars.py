from core.core.utils.collections import deep_update
from core.core.utils.settings import get_settings_from_environment

"""
    This takes in the environment variables with a matching prefix, strips out the prefix, and adds it to the global 

    For example:

    export CORESETTINGS_IN_DOCKER=true (environment variable)

    Could then be refrenced as a global as:
    IN_DOCKER (where the value would be true)
"""

# globals() is a dictionary of global variables
deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))       # type: ignore # noqa: F821
