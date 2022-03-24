import turtle

window = turtle.Screen()
window.title("Pong by Tre (HIRE ME)")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


#Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("purple")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)

#paddle B 
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("blue")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)

ball.dx = .15
ball.dy = .15


#paddle movements
def paddle1up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle2up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)


window.listen()
window.onkeypress(paddle1up, "w")
window.onkeypress(paddle1down, "s")
window.onkeypress(paddle2up, "Up")
window.onkeypress(paddle2down, "Down")

#Score 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


score1 = 0
score2 = 0
pen.write("Player 1: {}    (Use WASD and Arrow keys)    Player 2 : {}".format(score1, score2), align="center", font=("Courier", 16, "normal"))

#main
while True:
    window.update()

    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #wall hit
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player 1: {}    (Use WASD and Arrow keys)    Player 2 : {}".format(score1, score2), align="center", font=("Courier", 16, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player 1: {}    (Use WASD and Arrow keys)    Player 2 : {}".format(score1, score2), align="center", font=("Courier", 16, "normal"))

    #paddle collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor()< paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor()< paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1
