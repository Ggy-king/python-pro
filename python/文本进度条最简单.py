#文本进度条最简单
import time
scale = 10 #scale表示进度条精度
print("------执行开始------")
for i in range(scale + 1):
    a,b = '**' * i,'..' * (scale - i)
    c = (i/ scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.5) #每隔0.5秒执行一次 
print("------执行结束------")
