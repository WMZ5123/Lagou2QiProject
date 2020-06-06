def fun1(num1):
    num1 = num1 + 1
    return num1


# 有参数有返回值

def fun2(num2=1):
    return num2 + 1


# 无参数有返回值

def fun3(num3):
    num3 = num3 + 1


# 有参数无返回值

def fun4(num4=1):
    num4 = num4 + 1


# 无参数无返回值

if __name__ == '__main__':
    print(fun1(1))  # 结果为2，即返回值为输入值+1
    print(fun2())  # 结果为1，即返回值为默认值+1
    print(fun3(1))  # 结果为None，即返回值为空
    print(fun4())  # 结果为None，即返回值为空
