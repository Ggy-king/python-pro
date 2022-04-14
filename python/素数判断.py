# Python 程序用于检测用户输入的数字是否为质数 
# 用户输入数字
d = int(input("请输入一个数字: "))
# 质数大于 1
if d > 1:
   # 查看因子
   for i in range(2,d):
       if (d % i) == 0:
           print(d,"不是质数")
           break
   else:
       print(d,"是质数")
       
# 如果输入的数字小于或等于 1，不是质数
else:
   print(d,"不是质数")
