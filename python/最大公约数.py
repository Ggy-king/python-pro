#最大公约数
a = eval(input())
b = eval(input())
def f(a,b):
    c = max(a,b)
    d = min(a,b)
    if c % d == 0:
        return d
    for i in range(d//2,1,-1):  #这样写可以求出最大的数，即反过来求666
        if c % i == 0 and d % i == 0:
            return i
    return 1
print(f(a,b))
         
        
