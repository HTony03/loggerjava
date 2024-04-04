import sys
import traceback
import inspect
import os


def format_traceback_frame(frame):
    filename = frame[0]
    lineno = frame[1]
    name = frame[2]
    text = frame[3]

    # 移除文件路径，只保留文件名
    filename = os.path.basename(filename)

    # 移除函数名前的 'at '，并添加 ' in ' 来更接近 Java 风格
    name = name.replace('at ', '').replace(' in ', '')

    # 格式化输出
    return f"    at {name} ({filename}:{lineno})\n"


def handler(exc):
    """
    the handler of the exceptions
    :param exc: the catched Exception
    see README.md for the usage of it
    :return:
    """
    # 初始化输出字符串
    output = ""

    # 捕获异常类型和消息
    exc_type = type(exc).__name__
    exc_message = str(exc)

    # 添加异常类型和消息到输出字符串
    output += f"{exc_type}: {exc_message}\n"

    # 提取堆栈跟踪信息
    tb = traceback.extract_tb(exc.__traceback__)

    # 遍历堆栈帧并添加到输出字符串
    for frame in tb:
        output += format_traceback_frame(frame)

    return output


def handler2(Exception):
    # 获取异常的类型、值和traceback对象
    exc_type, exc_value, exc_traceback = sys.exc_info()
    # 格式化异常信息为字符串列表
    tb_list = traceback.format_exception(exc_type, exc_value, exc_traceback)
    # 将列表中的字符串连接起来形成完整的调用栈信息
    tb_str = ''.join(tb_list)
    # 打印调用栈信息
    print(f"捕获到异常: {Exception}\n调用栈信息:\n{tb_str}")
    print(exc_type.__name__)
    print(exc_value)
    print(exc_traceback)
    #print(tb_list)
    print(tb_str)

    exception_type_full_str = f"{type(Exception).__module__}.{type(Exception).__name__}"
    line = exception_type_full_str+": "+str(Exception)+"\n    at"
    print(line)

if __name__ == "__main__":
    try:
        print(a)
    except Exception as e:
        print(handler(e))
"""
        exception_type_name = type(e).__name__
        # 将异常类型的名称转化为字符串（实际上已经是字符串了）
        exception_type_str = str(exception_type_name)
        print(f"捕获到异常类型: {exception_type_str}")

        exception_type_full_str = f"{type(e).__module__}.{type(e).__name__}"
        print(f"完整的异常类型字符串: {exception_type_full_str}")

        tb = traceback.extract_tb(e.__traceback__)
        # 通常，最后一个元素是异常发生的位置
        last_frame = tb[-1]
        # 获取函数名和模块名
        func_name = last_frame[2]
        module_name = last_frame[0]

        print("捕获到异常:")
        print(f"异常类型: {type(e).__name__}")
        print(f"异常信息: {e}")
        print("调用栈信息:")
        # 打印完整的堆栈跟踪信息
        for frame in tb:
            filename, line_number, function_name, text = frame
            print(f"{module_name}.{function_name} (文件 {filename}, 行 {line_number})")
            print(f"    {text.strip()}")

        tb = e.__traceback__
        # 提取堆栈跟踪信息
        stack_info = traceback.extract_tb(tb)

        # 格式化堆栈跟踪信息以更接近Java的格式
        formatted_tb = []
        for frame in stack_info:
            filename, line_number, function_name, text = frame
            # 假设模块名就是文件名去掉.py后缀（这通常不是完全准确的，但在这里作为示例）
            module_name = filename.rsplit('.', 1)[0].replace('/', '.') if '.' in filename else '__main__'
            formatted_tb.append(f"{module_name}.{function_name} (文件 {filename}, 行 {line_number})")
            formatted_tb.append(f"    {text.strip()}")

            # 打印异常类型和消息
        print("捕获到异常:")
        print(f"异常类型: {type(e).__name__}")
        print(f"异常信息: {e}")

        # 打印格式化后的堆栈跟踪信息
        print("调用栈信息:")
        for line in formatted_tb:
            print(line)
"""