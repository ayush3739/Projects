from turtle import Screen,Turtle
from paddle import Pad
from ball import BALL
from scoreboard import Scoreboard
import time
sc=Screen()
sc.setup(width=800,height=600)
sc.bgcolor("black")
sc.title("PONG GAME")
sc.tracer(0)

r_paddle=Pad((350,0))
l_paddle=Pad((-350,0))
ball=BALL()
score= Scoreboard()



sc.listen() 
sc.onkey(r_paddle.upward,"Up")
sc.onkey(r_paddle.downward,"Down")
sc.onkey(l_paddle.upward,"w")
sc.onkey(l_paddle.downward,"s")

game_on=True
while game_on:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()
    #detect collision with wall
    if ball.ycor() >280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision with right paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    #detect  the wall after paddle for reset the game 

    if ball.xcor()>380 :
        ball.reset_posi()
        score.update_lscore()

    if ball.xcor()<-380:
        ball.reset_posi()
        score.update_rscore()
        






sc.exitonclick()

