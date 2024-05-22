# Copyright 2024 Open Source Robotics Foundation, Inc.
# Licensed under the Apache License, Version 2.0

from colcon_core.command \
    import LOG_LEVEL_ENVIRONMENT_VARIABLE \
    as COLCON_LOG_LEVEL_ENVIRONMENT_VARIABLE
from colcon_core.command import main as colcon_main
from colcon_core.environment_variable import EnvironmentVariable

"""Environment variable to set the log level"""
LOG_LEVEL_ENVIRONMENT_VARIABLE = EnvironmentVariable(
    'NEWCON_LOG_LEVEL',
    COLCON_LOG_LEVEL_ENVIRONMENT_VARIABLE.description)

"""Environment variable to set the configuration directory"""
HOME_ENVIRONMENT_VARIABLE = EnvironmentVariable(
    'NEWCON_HOME',
    'Set the configuration directory (default: ~/.newcon)')


def main(*args, **kwargs):
    """Execute the main logic of the command."""
    kwargs.setdefault('command_name', 'newcon')
    kwargs.setdefault('verb_group_name', 'newcon.verb')
    kwargs.setdefault(
        'environment_variable_group_name', 'newcon.environment_variable')
    return colcon_main(*args, **kwargs)
