import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


play=Player()
car=CarManager()
score=Scoreboard()

screen.listen()
screen.onkey(play.move_forward,'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_Cars()

    # detect the collision with the squares
    for cars in car.allcars:
        if cars.distance(play)<20:
            game_is_on=False
            score.game_over()
        
    # detetct player at finish line
    if play.check_finished():
        play.go_to_starT()
        car.level_up()
        score.increase_level()
    
        



screen.exitonclick()