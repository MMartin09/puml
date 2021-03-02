
import importlib
import pkgutil
import os
from types import ModuleType
from typing import List


def get_modules(path):
    # List holding all available modules
    modules: List[ModuleType] = []

    # Extract the name of the module
    module_name: str = os.path.basename(path)

    for _, name, is_pkg in pkgutil.walk_packages([path], f"{module_name}."):
        if not is_pkg:
            module: ModuleType = importlib.import_module(name)

            modules.append(module)

    return modules
