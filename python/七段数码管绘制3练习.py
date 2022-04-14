import turtle,datetime
def a():
    turtle.penup()
    turtle.fd(5)
def b(draw):
    a()
    turtle.down() if draw else turtle.penup()
    turtle.fd(40)
    a()
    turtle.right(90)
def c(d):
    b(True) if d in [2,3,4,5,6,8,9] else b(False)
    b(True) if d in [0,1,3,4,5,6,7,8,9] else b(False)
    b(True) if d in [0,2,3,5,6,8,9] else b(False)
    b(True) if d in [0,2,6,8] else b(False)
    turtle.left(90)
    b(True) if d in [0,4,5,6,8,9] else b(False)
    b(True) if d in [0,2,3,5,6,7,8,9] else b(False)
    b(True) if d in [0,1,2,3,4,7,8,9] else b(False)
    turtle.left(180)
    turtle.up()
    turtle.fd(20)
def e(date):
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('年',font("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font("Arial",18,"normal"))
        else:
            c(eval(i))
def main():
    turtle.setup(800,350,200,200)
    turtle.up()
    turtle.fd(-350)
    turtle.pensize(5)
    e(datetime.datetime.now().strftime('%Y-%m=%d+'))
    turtle.hideturtle()
main()
