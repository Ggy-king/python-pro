#我想练一下循环语
import turtle as u
u.setup(700,700,200,200)
u.penup()
u.goto(-300,0)
u.pensize(10)
u.pencolor('pink')
u.pendown()
u.seth(-90)
for j in range(10):
    u.circle(10,180)
    u.circle(-10,180)
u.done()