import turtle
import time
win=turtle.Screen()
win.title('simple analog clock')
win.bgcolor("white")
win.setup(width=800,height=600)
# create our pen
liner=turtle.Turtle()
liner.hideturtle()
liner.speed(0)
liner.pensize(3)

def draw_clock(h,m,s,liner):

    # pen clock face
    liner.up()
    liner.goto(0,210)
    liner.setheading(180)
    liner.color("black")
    liner.pendown()
    liner.circle(210)

    # Draw the lines for the hours
    liner.penup()
    liner.goto(0,0)
    liner.setheading(90)

    number_list =[i for i in range(1,13)]
    for draw in range(12):
        liner.forward(190)
        liner.write(number_list[draw])
        liner.pendown()
        liner.circle(1)
        liner.penup()
        liner.goto(0,0)
        liner.right(30)

    # draw the hour hand
    liner.penup()
    liner.goto(0,0)
    liner.color('black')
    liner.setheading(90)
    angle=(h/12)*360
    liner.right(angle)
    liner.pendown()
    liner.fd(80)

    # draw the minutes hand
    liner.penup()
    liner.goto(0, 0)
    liner.color('black')
    liner.setheading(90)
    angle = (m / 60) * 360
    liner.right(angle)
    liner.pendown()
    liner.fd(100)

    # draw the seconds
    liner.penup()
    liner.goto(0, 0)
    liner.color('black')
    liner.setheading(90)
    angle = (s / 60) * 360
    liner.right(angle)
    liner.pendown()
    liner.fd(180)
while True:
    h=int(time.strftime("%I"))
    m=int(time.strftime("%M"))
    s=int(time.strftime("%S"))
    draw_clock(h,m,s,liner)
    win.update()
    time.sleep(1)
    liner.clear()
win.mainloop()