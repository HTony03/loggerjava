import sys
import traceback
import inspect
import os

# 模块级别的变量，用于存储注册的类和函数信息
_database = []


def register_def(item):
    """
    register the classes/defs to the exceptionhander module
    :param item: the class/def you created
    :return: none
    """
    if inspect.isclass(item):
        class_name = item.__name__
        method_names = [method for method in dir(item) if callable(getattr(item, method)) and method[0] != "_"]
        _database.append({
            "name": class_name,
            "defs": method_names
        })
    elif inspect.isfunction(item):
        func_name = item.__name__
        _database.append({
            "name": func_name,
            "defs": []  # 函数没有内部方法，所以defs为空列表
        })
    else:
        raise ValueError("Only classes and functions can be registered.")


def query_def_ownership(def_name):
    """
    check the ownership of def_name
    :param def_name: the name of def
    :return: the ownership of the def
    """
    for entry in _database:
        if entry["name"] == def_name or def_name in entry["defs"]:
            return entry["name"]
    return None  # 如果没有找到，返回None


def handler(exc):
    """
    the handler of the exceptions
    :param exc: the caught Exception
    see README.md for the usage of it
    :return: none
    """
    exc_type = type(exc).__name__
    exc_message = str(exc)
    formatted_exc = f"{exc_type}: {exc_message}\n"

    tb = exc.__traceback__
    frames = traceback.extract_tb(tb)

    for frame in frames:
        filename, lineno, name, text = frame
        filename = os.path.basename(filename)

        cls = query_def_ownership(name)
        if cls is None:
            formatted_frame = f"    at {name} ({filename}:{lineno})\n"
        else:
            # formatted_frame = f"    at {module_name}.{cls}.{name} ({filename}:{lineno})\n"
            formatted_frame = f"    at {cls}.{name} ({filename}:{lineno})\n"

        formatted_exc += formatted_frame

    return formatted_exc


if __name__ == "__main__":
    pass
