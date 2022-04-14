#七段数码管绘制1
import turtle
def drawline(draw):  #绘制单段数码管
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawdight(d):  #根据数字绘制七段数码管
    drawline(True) if d in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if d in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if d in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if d in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.up()
    turtle.fd(20)
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawdight(8)
    turtle.hideturtle()
main()
    
