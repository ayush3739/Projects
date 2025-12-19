from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
sc=Screen()
sc.setup(width=600,height=600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)


snk=Snake()

food=Food()

score=Score()


sc.listen()
sc.onkey(snk.up,"Up")
sc.onkey(snk.down,"Down")
sc.onkey(snk.left,"Left")
sc.onkey(snk.right,"Right")


game_is_on=True
while game_is_on:
    sc.update()
    time.sleep(0.1)
    
    snk.move()
    #detect collision with food
    if snk.head.distance(food)<15:
        food.refresh()
        snk.extend()
        score.increase()

    #detect collision with wall
    if snk.head.xcor()>290 or snk.head.xcor()<-290 or snk.head.ycor ()>290 or snk.head.ycor() <-290:
        game_is_on=False
        score.game_over()

    #detect collision with tail
    # if head collide with any segment of a tail
    for seg in snk.segments[1:]:
        if snk.head.distance(seg) <10:
            game_is_on=False
            score.game_over()
    

        
  
    
        


sc.exitonclick()