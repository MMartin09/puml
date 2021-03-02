
import importlib
import pkgutil

import inspect

def test(cls):
    boring = dir(type("dummy", (object, ), {}))
    return [item
            for item in inspect.getmembers(cls)
            if item[0] not in boring]

def main():
    module_path: str = "../test_module/"

    for _, name, is_pkg in pkgutil.walk_packages([module_path], f"test_module."):
        print(name)
        print("")

        if not is_pkg:
            module = importlib.import_module(name)

            #for i in inspect(module):
            #    print(module)

            for key in dir(module):
                type = getattr(module, key)

                if inspect.isclass(type):
                    print(f"Found class: {key}")

                    print(test(type))

                    m = inspect.getmembers(type)
                    #print(m)

        print("---------------------\n")


if __name__ == '__main__':
    main()
