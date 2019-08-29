# 错位排列问题，递归调用

def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return (n - 1) * (f(n - 1) + f(n -2))
x = input("请输入钥匙数量：")
print(f(int(x)))
