from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)

        self.color('black')
        self.shape("turtle")
        self.penup()
        self.go_to_starT()
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)
    
    def go_to_starT(self):
        self.goto(STARTING_POSITION)

    def check_finished(self):
        if self.ycor()>280:
            return True
        else:
            return False


