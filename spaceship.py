from turtle import Turtle
from laser import Laser
from enemy import Enemy
import time
import random

class Spaceship(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.color("white")
        self.penup()
        self.setposition(position)
        self.laser_list = []
        self.enemy_list = []
        self.enemy_time = 0
        self.game = True


    def left(self):
        if self.xcor() > -350:
            # self.backward(10)
            self.setx(self.xcor() - 10)
    
    def right(self):
        if self.xcor() < 350:
            # self.forward(10)
            self.setx(self.xcor() + 10)
    
    def fire(self):
        laser = Laser(self.xcor(), self.ycor())
        self.laser_list.append(laser)

    def enemies(self):

        en = Enemy(random.randint(-350, 350), 370)
        self.enemy_list.append(en)
        # en.forward(20)


    def collosion(self):
        
        for laser in self.laser_list:
            x_laser, y_laser = laser.get_pos()
            if y_laser > 370:
                # print("HIGH")
                laser.clear()
                laser.hideturtle()
                self.laser_list.remove(laser)
            for en in self.enemy_list:
                x_en, y_en = en.get_pos() 

                if abs(y_laser - y_en) < 20 and abs(x_laser - x_en) < 20:
                    en.clear()
                    en.hideturtle()
                    self.enemy_list.remove(en)
                    laser.clear()
                    laser.hideturtle()
                    self.laser_list.remove(laser)




    def update(self):
        if time.time() - self.enemy_time > 1.2:
            self.enemies()
            self.enemy_time = time.time()

        for laser in self.laser_list:
            laser.move()
        for enemy in self.enemy_list:
            enemy.backward(0.04)
            x_en, y_en = enemy.get_pos()
            if y_en < -370:
                # print(y_en)
                self.game = False 
            if abs( y_en - self.ycor()) < 20 and abs(x_en - self.xcor()) < 20:
                self.game = False

        self.collosion()
   
