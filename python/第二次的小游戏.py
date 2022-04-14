"""这是第二次编一个小游戏"""
import random
a = random.randint(1,10)
counts = 3

while counts > 0 :
   c = input("你猜猜老子现在想的是一个什么数字:")
   b = int(c)
   
   if a == b :
     print("你挺牛逼的啊，竟然猜对了")
     break
   else :
     if b < a :
       print("小了")
     else :
       print("大了")
     counts = counts - 1
print("游戏结束！！！")
