from turtle import Turtle

class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-200, 0)

    def message(self, msg):
        self.write(msg, font=("Courier", 50, "bold"))