#最小公倍数
a = eval(input())
b = eval(input())
def f(a,b):
    c = max(a,b)
    d = min(a,b)
    if c % d == 0:
        return c
    for i in range(1,a*b+1):
        if i % c == 0 and i % d == 0:
            return i
    return a*b
print(f(a,b))
