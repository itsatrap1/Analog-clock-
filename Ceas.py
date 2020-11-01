import turtle
import time
from time import strftime

screen = turtle.Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.bgcolor("black")

# Clock features
clock = turtle.Turtle()
clock.speed(0)
clock.pensize(4)
clock.pencolor("green")


def mid_dot(circle):

    circle.goto(0, 0)
    circle.dot(10, "green")


def clock_hours(circle):

    circle.penup()
    circle.setheading(90)
    for hours in range(12):

        circle.goto(0, 0)
        circle.rt(30)
        if circle.heading() in [0, 90, 180]:
            circle.fd(215)
        else: circle.fd(225)
        circle.write(hours + 1, align = "center", font = ("Arial", 12, "bold"))


def draw_clock(circle, h, m, s):

    circle.ht()
    circle.penup()
    circle.goto(0, 200)
    circle.setheading(180)
    circle.pendown()
    circle.pencolor("green")
    circle.circle(200)
    circle.setheading(90)

    for i in range(12):

        circle.penup()
        circle.goto(0, 0)
        circle.rt(30)
        circle.fd(180)
        circle.pendown()
        circle.fd(20)

    # Hours

    circle.penup()
    circle.pencolor("purple")
    circle.goto(0, 0)
    circle.setheading(90)
    angle = (h / 12.0) * 360
    circle.rt(angle)
    circle.pendown()
    circle.fd(70)

    # Minutes

    circle.penup()
    circle.pencolor("yellow")
    circle.goto(0, 0)
    circle.setheading(90)
    angle = (m / 60.0) * 360
    circle.rt(angle)
    circle.pendown()
    circle.fd(110)

    # Seconds
    
    circle.penup()
    circle.pencolor("orange")
    circle.goto(0, 0)
    circle.setheading(90)
    angle = (s / 60.0) * 360
    circle.rt(angle)
    circle.pendown()
    circle.fd(140)


while True:

    hour = int(strftime("%H"))
    minute = int(strftime("%M"))
    seconds = int(strftime("%S"))
    draw_clock(clock, hour, minute, seconds)
    mid_dot(clock)
    clock_hours(clock)

    time.sleep(1)
    screen.update()
    clock.clear()
