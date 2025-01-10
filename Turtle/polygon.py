import turtle
turtle.Screen().setup(300,400)
turtle.Screen().bgcolor("blue")
turtle.speed(5)
polygon=turtle.Turtle()

num_sides=8
length=60
angle=360/num_sides
for i in range(num_sides+1):
    polygon.forward(length)
    polygon.right(angle)

turtle.done()
