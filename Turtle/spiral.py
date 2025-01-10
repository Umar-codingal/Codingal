import turtle
turtle.Screen().setup(300,400)
turtle.Screen().bgcolor("red")
pen=turtle.Turtle()

size=0
while True:
    for i in range (4):
        pen.forward(size+1)
        pen.left(90)
        size=size-5
    size+=1


turtle.done()
