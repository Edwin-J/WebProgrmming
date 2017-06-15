import turtle as t

t.speed(0)
t.hideturtle()

t.fillcolor("yellow")

t.begin_fill()
t.forward(50)
t.circle(50, 100)

t.right(100)
t.forward(30)

t.right(60)
t.circle(-120, 60)

t.right(60)
t.forward(100)

t.left(90)
t.forward(10)

t.left(90)
t.forward(65)

t.right(90)
t.forward(30)

t.right(50)
t.circle(-100, 80)

t.right(50)
t.forward(70)

t.right(20)
t.circle(-50, 58)

t.end_fill()

t.penup()
t.goto(60, 8)
t.fillcolor("blue")
t.pendown()

t.begin_fill()
t.left(168)
t.forward(50)
t.circle(50, 100)

t.right(100)
t.forward(30)

t.right(60)
t.circle(-120, 60)

t.right(60)
t.forward(100)

t.left(90)
t.forward(10)

t.left(90)
t.forward(65)

t.right(90)
t.forward(30)

t.right(50)
t.circle(-100, 80)

t.right(50)
t.forward(70)

t.right(20)
t.circle(-50, 58)

t.end_fill()

t.penup()
t.goto(-10, 110)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(67, -80)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
