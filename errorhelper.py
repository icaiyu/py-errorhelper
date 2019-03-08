# encoding: utf-8
import atexit
import sys
import json
if sys.version_info.major == 3:
    from io import StringIO
else:
    from cStringIO import StringIO


ERRORHELPERERRORS = u'''{
            "StopIteration":["迭代停止","迭代器不能再通过next返回元素的时候引起该错误"],
            "StopAsyncIteration":["异步迭代停止","异步迭代器不能通过__next__()返回元素引起该错误"],
            "FloatingPointError":["浮点错误","浮点运算失败时引发 始终定义此异常，但只能在使用--with-fpectl选项配置Python或在pyconfig.h文件中定义WANT_SIGFPE_HANDLER符号时引发此异常"],
            "ZeroDivisionError":["零除错误","零作为除数进行运算"],
            "OverflowError":["溢出错误","当算术运算的结果太大而无法表示时引发"],
            "AssertionError":["断言错误","当 assert 断言声明出错时引发的错误"],
            "AttributeError":["属性错误","引用属性或者赋值失败"],
            "BufferError":["缓冲错误","无法执行与缓冲区相关的操作时引发"],
            "EOFError":["文件结束错误","当input()函数没有读取任何数据便遇到文件结束符EOF"],
            "ImportError":["引用错误","当import声明没能找到相应的模块，或者 from ... 或者 import 没有找到模块中相应的名字"],
            "LookupError":["查询错误","在映射查询和序列查询失败时引发的错误，是 IndexError,KeyError 的基类,可能是由codecs.lookup()直接引起的"],
            "IndexError":["索引错误","序列的索引号超出该序列规定的长度或范围"],
            "KeyError":["键错误","映射(如字典dict映射)的键不在相应的集合中"],
            "MemoryError":["内存错误","运算超出内存范围"],
            "NameError":["名称错误","本地或者全局名称没有找到对应的变量名称","反馈的信息中包含了那个无效的名字"],
            "UnboundLocalError":["未绑定本地错误","引用函数或方法中的局部变量时引发，但没有值绑定到该变量是 NameError的子类"],
            "OSError":["系统错误","当系统函数返回与系统相关的错误时会引发此异常，包括IO失败，例如找不到文件或磁盘已满"],
            "BlockingIOError":["操作某对象(如socket)遇到阻塞的时候引发"],
            "ChildProcessError":["子进程错误","操作子进程失败"],
            "ConnectionError":["连接错误"],
            "BrokenPipeError":["坏管道错误","在写入管道的时候另一端已经关闭时引发的错误，或者试图对一个关闭的socket写入时引发的错误"],
            "ConnectionAbortedError":["连接终止错误","连接尝试被对方终止时引发的错误"],
            "ConnectionRefuseError":["连接拒绝错误","连接被对方拒绝引发的错误"],
            "ConnectionResetError":["连接重置错误","连接被对方重置时引发的错误"],
            "FileExistsError":["文件存在错误","试图创建一个已经存在的文件时引发错误"],
            "FileNotFoundError":["文件未找到错误","请求一个未存在的文件或路径"],
            "InterruptedError":["中断错误","系统调用被输入信号中断时触发"],
            "IsADirectoryError":["是一个路径错误","本该操作于文件的操作在路径上出发错误"],
            "NotADirectoryError":["不是一个文件操作","本该操作于路径上的操作于别的对象上了"],
            "PermissionError":["权限错误","操作没有足够的权限，比如没有文件系统的访问权"],
            "ProcessLookupError":["进程查找错误","找不到给的进程"],
            "TimeoutError":["超时错误","系统层面的系统函数操作超时触发"],
            "ReferenceError":["引用错误","当weakref.proxy()","函数创建的弱引用代理用于在垃圾回收后访问引用属性时引发此异常有关弱引用的更多信息，请参阅weakref模块"],
            "RuntimeError":["运行时错误","错误不能归为其他的任何类型时触发"],
            "NotImplementedError":["未实现错误","在用户定义的基类中，抽象方法在需要派生类覆盖方法时应引发此异常"],
            "RecursionError":["递归错误","递归达到了系统设置顶最大递归层次，可能是代码有bug的递归没有结束语句无穷无尽地递归，也可能真的是需要递归的层次太大，可以用sys.getrecursionlimite()查看最大层次"],
            "SyntaxError":["语句错误","编译器的解析器遇到语法错误时引发，您可能写个了bug"],
            "IndentationError":["缩进错误"],
            "TabError":["tab错误","您可能混用了tab键和空格键"],
            "SystemError":["系统错误","当解释器发现内部错误时引发，出现该错误请找专家"],
            "TypeError":["类型错误","将操作或函数作用于不适当类型的对象","关联值是一个字符串，提供有关类型不匹配的详细信息"],
            "ValueError":["值错误","当内置操作或函数接收到具有正确类型但不适当值的参数时引发，并且情况不会由更准确的异常（如 IndexError）描述"],
            "UnicodeError":["unicode错误","unicode相关的编码和解码错误"],
            "UnicodeEncodeError":["unicode编码错误","unicode在编码的时候引起的错误"],
            "UnicodeDecodeError":["unicode解码错误","unicode在解码的时候引起的错误"]
         }'''






if __name__ != '__main__':
    errorhlper_olderr = sys.stderr
    sys.stderr = errorhelper_recorder = StringIO()

    @atexit.register
    def helper():
        msg = errorhelper_recorder.getvalue()
        if not msg:
            return

        errors = json.loads(ERRORHELPERERRORS)

        for k, v in errors.items():
            if k in msg:
                msg += edit_info(k,v)
                break
        else:
            msg += edit_info(u"oh,还没翻译这个错误",["",u"您可以向 icaiyu@163.com 报告该错误，以便添加进errorhelper的新版本中",""])
        errorhlper_olderr.write(msg)
        exit()

    def edit_info(k,v):
        prefix = u"\n************************** 错误提示助手 **************************\n"
        subfix = u"\n******************************************************************"
        s = ""
        s += k + ":" + v[0] + "\n"
        s += v[1]
        return prefix + s + subfix


'''
TODO:
class MySTringIO(StringIO):

    def __init__(self):
        super(MySTringIO, self).__init__()

    def write(self, s):
        super(MySTringIO, self).write(s)
        for k, v in errors.items():
            if k in s:
                print('any error?')
                exit(0)
        #print("writing something")
'''