# Yanis Boudjeam IT3038C Project 2 11/01/223

# Snake Game
# Followed TokyoEdtech's Snake Game tutorial on youtube (https://www.youtube.com/playlist?list=PLlEgNdBJEO-n8k9SR49AshB9j7b5Iw7hZ)


#Import modules
import turtle
import time
import random

tickTime = 0.05

# Scoring
currentScore = 0
highScore = 0

# Window setup with turtle
window = turtle.Screen()
window.title("YB Snake Game - IT3038C Project 2")
window.bgcolor("red")
window.setup(width=1000, height=1000)
window.tracer(0)

# Snake body creation
snakeHead = turtle.Turtle()
snakeHead.turtlesize(1.5)
snakeHead.speed(0)
snakeHead.shape("square")
snakeHead.color("white")
snakeHead.penup()
snakeHead.goto(0, 0)
snakeHead.direction = "stop"

# Snake Pellets
pellet = turtle.Turtle()
pellet.turtlesize(1.5)
pellet.speed(0)
pellet.shape("circle")
pellet.color("black")
pellet.penup()
pellet.goto(0, 200)

bodySegments = []

scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.shape("square")
scoreBoard.color("yellow")
scoreBoard.penup()
scoreBoard.ht()
scoreBoard.goto(0, 450)
scoreBoard.write("Score: 0 | Snake Length: 1 | High Score: 0", align="center", font=("Impact", 30, "normal"))


# Functions
def snakeMove():
    # Moves the snake
    speed = 20

    if snakeHead.direction == "up":
        y = snakeHead.ycor()
        snakeHead.sety(y + speed)

    if snakeHead.direction == "down":
        y = snakeHead.ycor()
        snakeHead.sety(y - speed)

    if snakeHead.direction == "left":
        x = snakeHead.xcor()
        snakeHead.setx(x - speed)

    if snakeHead.direction == "right":
        x = snakeHead.xcor()
        snakeHead.setx(x + speed)


def move_up():
    if snakeHead.direction != "down":
        snakeHead.direction = "up"


def move_down():
    if snakeHead.direction != "up":
        snakeHead.direction = "down"


def move_left():
    if snakeHead.direction != "right":
        snakeHead.direction = "left"


def move_right():
    if snakeHead.direction != "left":
        snakeHead.direction = "right"


# Keybinds
window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

# Game Loop
while True:
    window.update()

    # Check for wall collision
    if snakeHead.xcor() > 490 or snakeHead.xcor() < -490 or snakeHead.ycor() > 490 or snakeHead.ycor() < -490:
        time.sleep(1)
        snakeHead.goto(0, 0)
        snakeHead.direction = "stop"

        # Get rid of previous segments
        for bodySegment in bodySegments:
            bodySegment.goto(1500, 1500)

        # Clear previous segment list
        bodySegments.clear()

        # Reset scoreboard
        currentScore = 0
        snakeLength = 1
        scoreBoard.clear()
        scoreBoard.write("Score: {} | Snake Length {} | High Score: {}".format(currentScore, snakeLength, highScore),align="center", font=("Impact", 30, "normal"))

        # Reset tick time
        tickTime = .05

    # Check for snake / pellet collision
    if snakeHead.distance(pellet) < 30:
        x = random.randint(-490, 490)
        y = random.randint(-490, 490)
        pellet.goto(x, y)

        # Add body segment
        new_bodySegment = turtle.Turtle()
        new_bodySegment.turtlesize(1.5)
        new_bodySegment.speed(0)
        new_bodySegment.shape("square")
        new_bodySegment.color("cyan")
        new_bodySegment.penup()
        bodySegments.append(new_bodySegment)

        # Decrease tick time
        tickTime -= 0.001

        # Increment score
        currentScore += 5
        snakeLength = (len(bodySegments)) + 1

        if currentScore > highScore:
            highScore = currentScore

        scoreBoard.clear()
        scoreBoard.write("Score: {} | Snake Length {} | High Score: {}".format(currentScore, snakeLength, highScore),align="center", font=("Impact", 30, "normal"))

    # Move end segments
    for index in range(len(bodySegments) - 1, 0, -1):
        x = bodySegments[index - 1].xcor()
        y = bodySegments[index - 1].ycor()
        bodySegments[index].goto(x, y)

    # Move the segment next to head
    if len(bodySegments) > 0:
        x = snakeHead.xcor()
        y = snakeHead.ycor()
        bodySegments[0].goto(x, y)

    snakeMove()

    # Check for snake body collision
    for bodySegment in bodySegments:
        if bodySegment.distance(snakeHead) < 20:
            time.sleep(1)
            snakeHead.goto(0, 0)
            snakeHead.direction = "stop"

            # Get rid of previous segments
            for bodySegment in bodySegments:
                bodySegment.goto(1500, 1500)

            # Clear previous segment list
            bodySegments.clear()

            # Reset scoreboard
            currentScore = 0
            snakeLength = 1
            scoreBoard.clear()
            scoreBoard.write("Score: {} | Snake Length {} | High Score: {}".format(currentScore, snakeLength, highScore),
                             align="center", font=("Impact", 30, "normal"))
            # Reset tick time
            tickTime = .05

    time.sleep(tickTime)

window.mainloop()
