def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
num = eval(input("请输入一个整数："))
print(fact(abs(int(num))))
