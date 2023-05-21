from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# set up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

dash_line = Turtle()
dash_line.goto(0, 300)
dash_line.setheading(270)  # facing downward
dash_line.color("white")
dash_line.pensize(10)
dash_line.hideturtle()
for _ in range(30):
    dash_line.forward(30)
    dash_line.penup()
    dash_line.forward(30)
    dash_line.pendown()


# set up paddle, ball
r_paddle = Paddle("right")
l_paddle = Paddle("left")
ball = Ball()
score_board = ScoreBoard()

# set up event listener
screen.listen()
screen.onkey(r_paddle.up, key="Up")
screen.onkey(r_paddle.down, key="Down")
screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")


# start game
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # update after init paddle and ball, so that we won't see paddle moving from center to the side
    ball.move()

    # detect collision with top and bot edges
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect R paddle misses:
    if ball.xcor() > 400:
        ball.reset_position()
        score_board.l_point()

    # detect L paddle misses:
    if ball.xcor() < -400:
        ball.reset_position()
        score_board.r_point()


screen.exitonclick()
