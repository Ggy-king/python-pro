x = eval(input("黄金价格"))
y = eval(input("美元汇率"))
d = eval(input("黄金重量"))
b = d/31.1034768
a = x*b
c = a*y
print("黄金价值{:.2f}".format(c))
