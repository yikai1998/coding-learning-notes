# coding=gbk

# 简单版
def check(func):
    def inside(a, b):
        if b == 0:
            print('can not divide by 0')
            return 0
        print('Calculating...')
        return func(a, b)
    return inside


@check  # equals div = check(div)
def div(a, b):
    return a/b


print(div(5, 0))
print(div(1005001, 20))


# 增加难度
def check2(param=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in args:
                print(i)
            for k, v in kwargs.items():
                print(k, v)
            if param is not None:
                print(f'Applying {param} parameter to function {func.__name__}')
            # 在这里可以添加更多的逻辑，比如检查参数，或者根据param的值改变行为
            print(func(*args, **kwargs))
        return wrapper
    return decorator


# 使用装饰器，传入参数
@check2(param='special behavior')
def div(a, b):
    return a / b if b != 0 else 'Cannot divide by zero'


# 使用装饰器，不传入参数
@check2()
def add(a, b):
    return a + b


# 使用装饰器，传入不同的参数
@check2(param='another behavior')
def multiply(a, b, c='test'):
    return a * b


multiply(10, 30, c='can you see')
add(100, 2000)
div(490, 80)
'''
10
30
c can you see
Applying another behavior parameter to function multiply
300
100
2000
2100
490
80
Applying special behavior parameter to function div
6.125
'''
