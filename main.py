import turtle
from spaceship import Spaceship
from game_over import GameOver


screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title('Space Invaders')
screen.tracer(0)
screen.listen()


spaceship = Spaceship((0, -350)) 
gameover = GameOver()


screen.onkeypress(spaceship.left, 'a')
screen.onkeypress(spaceship.right, 'd')
screen.onkeypress(spaceship.fire, 'space')


game_on = True

while game_on:

    spaceship.update()
    screen.update()
    if spaceship.game == False:
        gameover.message("GAME OVER")
        spaceship.hideturtle()
        # break
        #  
    # if spaceship.get_pos() > 350:
    #     spaceship.remove() 
    
    
    


