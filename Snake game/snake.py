from turtle import Turtle
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    x_posi=[0,-20,-40]
    segments=[]
    move_dist=20
    
    
    def __init__(self):
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for i in self.x_posi:
            self.add_segment((i, 0))
            

    def add_segment(self, position):
        tim = Turtle()
        tim.color('white')
        tim.shape('square')
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x=self.segments[i-1].xcor()
            new_y=self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.segments[0].forward(self.move_dist)
    
    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() !=LEFT:    
            self.head.setheading(RIGHT)
        