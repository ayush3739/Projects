from turtle import Turtle, Screen
import random
is_on=True
screen = Screen()
screen.setup(width=500,height=400)

ask=screen.textinput(title="Make your bet",prompt="which turtle will win the race? enter a color: ")
colors=['red','orange','yellow','green','blue','purple']
y_positions=[-70,-40,-10,20,50,80]

all_turtles=[]
for i in range(5):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[i])
    all_turtles.append(new_turtle)


if ask:
    is_on=True

while is_on:
    for i in all_turtles:
        if i.xcor()>230:
            won=i.pencolor()        
            if ask==won:
                print(f"You've won! the {won} turtle is the winner!")
            else:
                print(f"You lost! the {won} turtle is the winner!")
            is_on=False
            
        rand_distance=random.randint(0,10)
        i.forward(rand_distance)



screen.exitonclick()