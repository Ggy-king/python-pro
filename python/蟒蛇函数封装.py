#e2.3DrawPython.py
import turtle
def drawSnake(radius,angle,length):
    turtle.seth(-40)
    for i in range(length):
      turtle.circle(radius,angle)
      turtle.circle(-radius,angle)
    turtle.circle(radius,angle/2)
    turtle.fd(40)
    turtle.circle(16,180)
    turtle.fd(40*2/3)
turtle.setup(650,350,200,200)
turtle.up()
turtle.fd(-250)
turtle.down()
turtle.pensize(35)
turtle.pencolor(0,0,0)
drawSnake(40,80,4)
turtle.done