import turtle
import time as ti


t=turtle.Turtle()



def square(y):
    for i in range(4):
        t.forward(y)
        t.left(90)

sizevar=1
for x in range(10,50):
    square(sizevar)
    sizevar+=6
    t.penup()
    t.backward(3)
    t.right(90)
    t.forward(3)
    t.left(90)
    t.pendown()
''' concentric circles '''
r=10
for i in range(20):
    t.circle(r * i)
    t.up()
    t.sety((r * i)*(-1))
    t.down()










ti.sleep(5)
