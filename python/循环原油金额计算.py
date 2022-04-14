#循环原油金额计算
x = eval(input("请输入原油价格"))
y = input("请输入原油数量")
while y not in ['n','N']:
 if y[-1] in ['l']:
    c = x*eval(y[0:-3])
    print("{:.2f}".format(c))
 elif y[-1] in ['t']:
    d = 1/0.14*x*eval(y[0:-1])
    print("{:.2f}".format(d))
 else :
    print("输入格式错误")
 y = input("请输入原油数量")
    
