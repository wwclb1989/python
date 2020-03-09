__all__ = ["add", "sub"]

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b:
        return a / b
    else:
        print('error')

# 若当前模块是启动模块，则__name__的值为文件名
if __name__ == "__main__":
    print(add(3, 4))
    print(sub(3, 4))
else:
    print("__name__")