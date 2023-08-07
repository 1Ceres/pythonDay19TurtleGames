from turtle import Turtle, Screen


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def left():
    t.left(5)


def right():
    t.right(5)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


t = Turtle()
screen = Screen()
screen.listen()
screen.onkey(move_forward, "Right")
screen.onkey(move_backward, "Left")
screen.onkey(left, "Up")
screen.onkey(right, "Down")
screen.onkey(clear, "c")
screen.exitonclick()
