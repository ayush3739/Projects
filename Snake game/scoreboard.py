from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.sco=0
        self.color('white')
        self.penup()
        self.goto(x=0,y=270)
        
        self.write(f"score: {self.sco}",align="center",font=('courier',24,"normal"))
        
        self.hideturtle()
        
    def increase(self):
        self.sco+=1
        self.clear()
        self.write(f"score: {self.sco}",align="center",font=('Arial',24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=('Arial',24,"normal"))
