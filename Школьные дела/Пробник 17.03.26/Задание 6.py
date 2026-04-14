from turtle import *
tracer(0)
koef = 20

for _ in range(2):
    forward(5 * koef)
    left(90)
    backward(13 * koef)
    left(90)
up()

backward(10 * koef)
right(90)
forward(9 * koef)
left(90)

down()

for _ in range(2):
    forward(11 * koef)
    right(90)
    forward(7 * koef)
    right(90)


up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()