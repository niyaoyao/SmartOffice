def handle_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"捕获到异常: {e}")
            # 可以在这里添加其他处理逻辑，比如记录日志、返回特定值等
    return wrapper

# 使用装饰器修饰需要进行异常处理的函数
@handle_exception
def example_function():
    # 可能引发异常的函数体
    result = 10 / 0  # 除以零会引发 ZeroDivisionError 异常

# 调用经过装饰器修饰后的函数
example_function()
