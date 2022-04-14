#黄金换算
x = eval(input("黄金价格"))
y = eval(input("黄金汇率"))
d = eval(input("黄金数量"))
b = d/31.1034768
a = x*b
c = a*y
print("{:.3f}".format(c))
