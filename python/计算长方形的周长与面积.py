#计算长方形的周长与面积
x = eval(input("请输入长"))
y = eval(input("请输入宽"))
c = 2*x+2*y
d = x*y
print("长方形的周长是{:.2f}".format(c))
print("长方形的面积是{:.2f}".format(d))
