from turtle import Turtle


class Laser(Turtle):

    def __init__(self, x, y):
    
        
        super().__init__()

        self.color("red")
        self.penup()
        self.hideturtle()
        self.setposition(x, y)
        self.setheading(90)
        self.forward(10)
        self.pendown()
        self.pensize(5)
        

    def move(self):

        self.clear()
        self.forward(1)
        self.forward(1)
        self.forward(-1)
    
    def get_pos(self):
        return self.xcor(), self.ycor()


