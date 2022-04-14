#import turtle = form turtie import* = import turtle as t
import turtle as t
#建立坐标系turtle.setup(width,height,startx,starty)
t.setup(650,350,200,200)
#抬笔落笔设宽度与颜色 改变绝对角度
t.penup()
t.fd(-250)
t.pendown()
t.pensize(25)
t.pencolor("red")
t.seth(-40)
#进入循环语句用for和in语句
for u in range(4):
  t.circle(40,80)
  t.circle(-40,80)
#循环之后开始绘制蛇头与颈部
t.circle(40,80/2)
t.fd(40)
t.circle(16,90)
t.fd(40*2/3)
t.done()

