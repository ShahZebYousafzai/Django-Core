

import yaml


def yaml_coerce(value):
    # Convert value to proper Python
    if isinstance(value, str):

        # yaml.load returns a Python object (we are just creating some quick yaml data)
        # Creates string dict "{'apples': 1, 'bacon': 2}" to Python dict
        # Useful because sometimes we need to stringify settings this way
        # (like in Dockerfile)
        return yaml.load(f'dummy: {value}', yaml.SafeLoader)['dummy']

    return value
