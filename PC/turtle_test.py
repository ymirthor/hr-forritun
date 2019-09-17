import turtle
from random import randint

a=turtle.Screen()
a.bgcolor('black')
a.title('Night Sky')
a.screensize()
a.setup(width = 1.0, height = 1.0)


dreamy=turtle.Turtle()
dreamy.color('white')
dreamy.pensize(0)
dreamy.hideturtle()
dreamy.speed(100)

def random_star():
    size=randint(1,15)    
    dreamy.begin_fill()
    for x in range(5):
        
        dreamy.forward(size)
        dreamy.right(144)
    dreamy.end_fill()
def random_position():
    dreamy.penup()
    y=randint(-540,540)
    x=randint(-960,960)
    dreamy.goto(x,y)
    dreamy.pendown()

for x in range(500):
    random_star()
    random_position()
