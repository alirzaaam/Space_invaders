from turtle import Turtle
import random 
class Enemy(Turtle):
    def __init__(self, x, y):
        super().__init__()  
        self.shape('circle')
        self.color(random.random(), random.random(), random.random())
        self.penup()
        self.setheading(90)
        self.goto(x, y)
        self.visibility = False


    def get_pos(self):
        return self.xcor(), self.ycor()

    def remove(self):
        self.reset()
        self.visibility = True
        return self.visibility
