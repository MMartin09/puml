import importlib
import pkgutil
import inspect
from types import ModuleType
import os
from puml.templates import *
from puml.accessor import Accessor
from puml.module_helper import get_modules, get_module_attributes





def main():
    module_path: str = "../test_module/"
    module_path = os.path.normpath(module_path)

    modules = []
    modules = get_modules(module_path)

    for module in modules:
        for key in dir(module):
            module_type = getattr(module, key)

            if inspect.isclass(module_type):
                attr = []
                vars = get_module_attributes(module_type)

                for name, value in vars.items():
                    pos_1 = str(value).find("'", 0)
                    pos_2 = str(value).find("'", pos_1 + 1)
                    val = str(value)[pos_1 + 1 : pos_2]

                    # Python default
                    accessor = Accessor.Public

                    #                    name = k

                    if name.startswith("__"):
                        name = name[2:]
                        accessor = Accessor.Private
                    elif name.startswith("_"):
                        name = name[1:]
                        accessor = Accessor.Protected

                    attr.append(
                        Attr_Template.render(
                            accessor=accessor.value, name=name, type=val
                        )
                    )

                print(Class_Template.render(class_name=key, attrs=attr))
                print("")

    #
    # for _, name, is_pkg in pkgutil.walk_packages([module_path], f"test_module."):
    #     if not is_pkg:
    #         module: ModuleType = importlib.import_module(name)
    #
    #         # return
    #         # for key in dir(module):
    #         #     classname = key
    #         #     type = getattr(module, key)
    #         #
    #         #     if inspect.isclass(type):
    #         #         attr = []
    #         #
    #         #         vars = test(type)[0][1]
    #         #         vars = dict(vars)
    #         #
    #         #         for key, value in vars.items():
    #         #             pos_1 = str(value).find("'", 0)
    #         #             pos_2 = str(value).find("'", pos_1+1)
    #         #             val = str(value)[pos_1+1:pos_2]
    #         #
    #         #             attr.append(Attr_Template.render(name=key, type=val))
    #         #             #print(val)
    #         #
    #         #         print(Class_Template.render(class_name=classname, attrs=attr))
    #         #         print("")
    #         #
    #         #         #print(Class_Template.render(class_name=f"{name}.{key}", attrs=[]))
    #
    # # for _, name, is_pkg in pkgutil.walk_packages([module_path], f"test_module."):
    # #     print(name)
    # #     print("")
    # #
    # #     if not is_pkg:
    # #         module = importlib.import_module(name)
    # #
    # #         #for i in inspect(module):
    # #         #    print(module)
    # #
    # #         for key in dir(module):
    # #             type = getattr(module, key)
    # #
    # #             if inspect.isclass(type):
    # #                 print(f"Found class: {key}")
    # #
    # #                 print(test(type)[0][1])
    # #
    # #                 m = inspect.getmembers(type)
    # #                 #print(m)
    # #
    # #     print("---------------------\n")


if __name__ == "__main__":
    main()
