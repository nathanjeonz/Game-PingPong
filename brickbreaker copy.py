import turtle
from turtle import Screen, ontimer
from rod import Rod
from brick import BrickGroup  

from ball import Ball


bottom_rod = Rod(x=0,y=-500,hdn=0)

def move_left():
    bottom_rod.forward(50)

def move_right():
    bottom_rod.forward(-50)



screen = Screen()
screen.tracer(0)  # Disable automatic screen updates for smoother animation
screen.setup(1600, 1000)
turtle.listen()
turtle.onkeypress(move_left,'Right')
turtle.onkeypress(move_right,'Left')

bg = BrickGroup(  [-700,700],[500,0]  )
b = Ball(0,0,color ='red')

# Main game loop
def game_loop():
    # Move rods based on key state
    
    # Move ball
    b.movement()

    # Collision with top/bottom walls
    if b.ycor() > 490 or b.ycor() < -490:
        b.reverse_y()
    if b.xcor() > 800 or b.xcor() < -800:
        b.reverse_x()

    # Collision with paddles
    if b.distance(bottom_rod) < 50:
        b.reverse_y()

    # Game over
    if b.xcor() > 800 or b.xcor() < -800:
        print("Game Over")
        return
    screen.update()
    ontimer(game_loop, 8)  # Run approx 60 FPS

# Start game loop
game_loop()
screen.mainloop()









turtle.mainloop()



