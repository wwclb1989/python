# 打印出15以内的所有质数
i = 1
while i <= 15:
    i += 1
    j = 1
    while j < i - 1:
        j += 1
        if i % j != 0:
            continue
        else:
            break
    else:
        print(i)