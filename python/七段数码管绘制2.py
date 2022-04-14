#七段数码管绘制2
import turtle,datetime
def a(aa):
    turtle.down() if aa else turtle.up()
    turtle.fd(40)
    turtle.right(90)
def b(bb):
    a(True) if bb in [2,3,4,5,6,8,9] else a(False)
    a(True) if bb in [0,1,3,4,5,6,7,8,9] else a(False)
    a(True) if bb in [0,2,3,5,6,8,9] else a(False)
    a(True) if bb in [0,2,6,8] else a(False)
    turtle.left(90)
    a(True) if bb in [0,4,5,6,8,9] else a(False)
    a(True) if bb in [0,2,3,5,6,7,8,9] else a(False)
    a(True) if bb in [0,1,2,3,4,7,8,9] else a(False)
    turtle.left(180)
    turtle.up()
    turtle.fd(20)
def c(cc):
    for i in cc:
        b(eval(i))
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    c(datetime.datetime.now().strftime('%Y%m%d'))
    turtle.hideturtle()
main()
    
