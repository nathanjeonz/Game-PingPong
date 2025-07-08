from rod2 import Rod2
from rod import Rod
from ball import Ball
from turtle import Screen, ontimer

screen = Screen()
screen.tracer(0)  # Disable automatic screen updates for smoother animation
screen.setup(1600, 1000)
screen.bgcolor("black")

# Create ball and rods
b = Ball(0, 0)
r = Rod(c='red')
r2 = Rod2(c='blue')

# Movement flags
keys = {"Up": False, "Down": False, "w": False, "s": False}

# Key handlers
def press_key(key):
    keys[key] = True

def release_key(key):
    keys[key] = False

# Bind keys
for key in keys:
    screen.onkeypress(lambda k=key: press_key(k), key)
    screen.onkeyrelease(lambda k=key: release_key(k), key)

screen.listen()

# Main game loop
def game_loop():
    # Move rods based on key state
    if keys["w"]:
        r.move_up()
    if keys["s"]:
        r.move_down()
    if keys["Up"]:
        r2.move_up2()
    if keys["Down"]:
        r2.move_down2()

    # Move ball
    b.movement()

    # Collision with top/bottom walls
    if b.ycor() > 490 or b.ycor() < -490:
        b.reverse_y()

    # Collision with paddles
    if b.distance(r) < 50:
        b.reverse_x()
    if b.distance(r2) < 50:
        b.reverse_x()

    # Game over
    if b.xcor() > 800 or b.xcor() < -800:
        print("Game Over")
        return
    screen.update()
    ontimer(game_loop, 8)  # Run approx 60 FPS

# Start game loop
game_loop()
screen.mainloop()
