import turtle
from random import randint

a=turtle.Screen()
a.bgcolor('black')
a.title('Night Sky')
a.screensize()
a.setup(width = 1.0, height = 1.0)


tim=turtle.Turtle()
tim.color('white')
tim.pensize(0)
tim.hideturtle()
tim.speed(100)

def random_star():
    size=randint(1,15)    
    tim.begin_fill()
    for x in range(5):
        
        tim.forward(size)
        tim.right(144)
    tim.end_fill()
def random_position():
    tim.penup()
    y=randint(-540,540)
    x=randint(-960,960)
    tim.goto(x,y)
    tim.pendown()

for x in range(500):
    random_star()
    random_position()
