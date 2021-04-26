import importlib
import pkgutil
import os
import inspect
from types import ModuleType
from typing import List


def get_modules(path):
    """

    Args:
        path (str):

    Returns:

    """

    # List holding all available modules
    modules: List[ModuleType] = []

    # Extract the name of the module
    module_name: str = os.path.basename(path)

    for _, name, is_pkg in pkgutil.walk_packages([path], f"{module_name}."):
        if not is_pkg:
            module: ModuleType = importlib.import_module(name)

            modules.append(module)

    return modules


def get_module_attributes(cls) -> dict:
    """Get user defined attributes.

    Source:
        https://stackoverflow.com/a/4241225/4685974

    Args:
        cls:

    Returns:

    """

    boring = dir(type("dummy", (object,), {}))
    attributes = [item for item in inspect.getmembers(cls) if item[0] not in boring]

    attributes = attributes[0][1]
    attributes = dict(attributes)

    return attributes
