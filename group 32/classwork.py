from turtle import begin_fill, color, end_fill, exitonclick, forward, goto, left, pendown, penup, right, speed, width



width(7)


color("orange")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()



forward(70)
begin_fill()
color("brown")
left(90)
forward(120)               #heigt of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(120, 120)
pendown()

color("brown")
begin_fill()
right(60)
forward(57)

begin_fill()
color("cyan")
begin_fill()
forward(55)
left(90)
forward(65)
left(90)
forward(55)
left(90)
forward(60)
end_fill()

penup()
goto(120, 120)
pendown()

right(90)
color("brown")
forward(15)

begin_fill()
color("cyan")
forward(57)
right(90)
forward(60)
right(90)
forward(60)
end_fill()


exitonclick()
                                                                                            