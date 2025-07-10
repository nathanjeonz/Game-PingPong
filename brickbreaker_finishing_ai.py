import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("#1e1e1e")
screen.setup(width=1600, height=1000)
screen.tracer(0)

# === ROD (PADDLE) ===
class Rod(turtle.Turtle):
    def __init__(self, x, y, length=200, color="#00BFFF"):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=length / 20)
        self.penup()
        self.goto(x, y)
        self.speed(0)

    def move(self, delta):
        new_x = self.xcor() + delta
        if -750 < new_x < 750:
            self.setx(new_x)

# === BALL ===
class Ball(turtle.Turtle):
    def __init__(self, x, y, color="red"):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.x_move = 4
        self.y_move = 4

    def movement(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def reverse_x(self):
        self.x_move *= -1

    def reverse_y(self):
        self.y_move *= -1

# === BRICK GROUP ===
class BrickGroup:
    def __init__(self, x_range, y_range, rows=5, cols=14):
        self.bricks = []
        colors = ["#FF6347", "#FFD700", "#00FF7F", "#1E90FF", "#DA70D6"]
        x_start, x_end = x_range
        y_start, y_end = y_range
        x_gap = (x_end - x_start) / (cols - 1)
        y_gap = (y_start - y_end) / (rows - 1)

        for row in range(rows):
            for col in range(cols):
                brick = turtle.Turtle()
                brick.shape("square")
                brick.shapesize(stretch_wid=1, stretch_len=3)
                brick.color(colors[row % len(colors)])
                brick.penup()
                brick.goto(x_start + col * x_gap, y_start - row * y_gap)
                self.bricks.append(brick)

# === SETUP OBJECTS ===
# Paddle
bottom_rod = Rod(x=0, y=-450)

# Ball
ball = Ball(x=0, y=0, color='#FF4500')

# Bricks
bricks = BrickGroup(x_range=[-700, 700], y_range=[300, 500])

# Game over text turtle
game_text = turtle.Turtle()
game_text.hideturtle()
game_text.color("white")
game_text.penup()

# === KEY CONTROLS ===
def move_left():
    bottom_rod.move(-40)

def move_right():
    bottom_rod.move(40)

screen.listen()
screen.onkeypress(move_left, 'Left')
screen.onkeypress(move_right, 'Right')

# === GAME LOOP ===
def game_loop():
    ball.movement()

    # Wall collision
    if ball.ycor() > 480:
        ball.reverse_y()
    if ball.xcor() > 780 or ball.xcor() < -780:
        ball.reverse_x()

    # Paddle collision
    if ball.distance(bottom_rod) < 60 and ball.ycor() < -420:
        ball.reverse_y()

    # Bottom = Game Over
    if ball.ycor() < -500:
        game_text.goto(0, 0)
        game_text.write("Game Over", align="center", font=("Arial", 36, "bold"))
        return

    # Brick collision
    for brick in bricks.bricks[:]:
        if ball.distance(brick) < 50:
            brick.hideturtle()
            bricks.bricks.remove(brick)
            ball.reverse_y()
            break

    screen.update()
    turtle.ontimer(game_loop, 10)

# Start the game loop
game_loop()
screen.mainloop()
