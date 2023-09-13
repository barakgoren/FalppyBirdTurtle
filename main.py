import random
import time
import turtle
from threading import Thread
from time import sleep
from Position import Position
from Cloud import Cloud

bird_gif = ["./Pics/bird.gif",
            "./Pics/bird2.gif",
            "./Pics/bird3.gif"]
# Set up the screen'
wn = turtle.Screen()
wn.title("Final Game Project")
wn.bgcolor("#3fd6e0")
wn.addshape(bird_gif[0])
wn.addshape(bird_gif[1])
wn.addshape(bird_gif[2])
wn.setup(700, 1.0)
wn.tracer(0)
pen = turtle.Turtle()
pen.speed(0)

bird_velocity_y = 0
jump_strength = 13
jump_strength_challenge = 7
bonus = False

isGameOver = False
pause = True

# Create the platforms
platforms = []
platforms_top = []
platform_positions = []

# Creating clouds
clouds = []

positions = [
    Position(top_width=20, top_y=275, bot_width=3, bot_y=-70),
    Position(top_width=19, top_y=285, bot_width=4, bot_y=-60),
    Position(top_width=18, top_y=295, bot_width=5, bot_y=-50),
    Position(top_width=17, top_y=305, bot_width=6, bot_y=-40),
    Position(top_width=16, top_y=315, bot_width=7, bot_y=-30),
    Position(top_width=15, top_y=325, bot_width=8, bot_y=-20),
    Position(top_width=14, top_y=335, bot_width=9, bot_y=-10),
    Position(top_width=13, top_y=345, bot_width=10, bot_y=0),
    Position(top_width=12, top_y=355, bot_width=11, bot_y=10),
    Position(top_width=11, top_y=365, bot_width=12, bot_y=20),
    Position(top_width=10, top_y=375, bot_width=13, bot_y=30),
    Position(top_width=9, top_y=385, bot_width=14, bot_y=40),
    Position(top_width=8, top_y=395, bot_width=15, bot_y=50),
    Position(top_width=7, top_y=405, bot_width=16, bot_y=60),
    Position(top_width=6, top_y=415, bot_width=17, bot_y=70),
    Position(top_width=5, top_y=425, bot_width=18, bot_y=80)
]


test = turtle.Turtle()
test.goto(0, 0)
test.penup()
test.sety(test.ycor()+75)


def display_game_over(points):
    wn.clear()
    wn.bgcolor("#3fd6e0")
    writer2 = turtle.Turtle()
    writer2.penup()
    writer2.color("white")
    writer2.goto(0, 0)
    writer2.hideturtle()
    writer2.write(f"   Game Over\nYour score is {points.__str__()}", align="center", font=("Comic Sans MS", 24, "normal"))


def turnleft():
    test.left(20)


def turnright():
    test.right(20)


def forward():
    test.forward(10)


def pause_game():
    global pause
    pause = not pause


def bonus_start():
    global bonus
    bonus = not bonus


obs = turtle.Turtle()
obs.penup()
obs.goto(50, 0)
obs.shape("square")

bird = turtle.Turtle()
bird.penup()
bird.sety(bird.ycor()+100)


def jump():
    global bird_velocity_y
    bird_velocity_y = jump_strength


def jump_challenge():
    global bird_velocity_y
    bird_velocity_y = jump_strength_challenge


def bird_fly():
    indicator = True
    while True:
        for frame in bird_gif:
            bird.shape(frame)
            sleep(0.08)


pen.penup()
pen.goto(-800, -100)
pen.pendown()
pen.fillcolor("#05a60a")
pen.pencolor("#05a60a")

pen.begin_fill()
for i in range(1, 3):
    pen.forward(1600)
    pen.right(90)
    pen.forward(75)
    pen.right(90)
pen.end_fill()

pen.fillcolor("#bfa22c")
pen.pencolor("#bfa22c")

pen.sety(pen.ycor()-50)
pen.begin_fill()
for i in range(1, 3):
    pen.forward(1600)
    pen.right(90)
    pen.forward(500)
    pen.right(90)
pen.end_fill()

wn.listen()
wn.onkeypress(jump_challenge, "space")
wn.onkeypress(jump, "w")
wn.onkeypress(turnleft, 'Left')
wn.onkeypress(turnright, 'Right')
wn.onkeypress(forward, 'Up')
wn.onkeypress(pause_game, 'P')
wn.onkeypress(pause_game, 'p')
wn.onkeypress(bonus_start, 'b')

index = 0
gif_frame = 0

obs.hideturtle()
test.hideturtle()

points = 0
timer = 0
clouds_timer = 79
challenge_counter = 0
counter_direction = 1
challenge_timer = 0
challenge_clock = 0
challenge_duaration = 0

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.goto(-300, 300)
writer.color("white")


def creating_clouds():
    clouds.append(Cloud(600, random.randint(50, 400)))


# Initialize Clouds
for i in range(0, 15):
    clouds.append(Cloud(random.randint(-600, 800), random.randint(50, 400)))

pos = random.randint(0, len(positions)-1)
cur_pos = positions[pos]
timer = 0
platform_bot = turtle.Turtle()
platform_bot.shape("square")
platform_bot.shapesize(stretch_wid=cur_pos.get_bot_width(), stretch_len=1)
platform_bot.color("green")
platform_bot.penup()
platform_bot.goto(400, cur_pos.get_bot_y())
platform2 = turtle.Turtle()
platform2.shape("square")
platform2.shapesize(stretch_wid=cur_pos.get_top_width(), stretch_len=1)
platform2.color("green")
platform2.penup()
platform2.goto(400, cur_pos.get_top_y())
platforms.append(platform_bot)
platforms_top.append(platform2)

platforms_speed = 2
platforms_creation = 60

while not isGameOver:
    while not pause and not isGameOver:
        wn.update()

        if bonus:
            platforms_speed = 40
            platforms_creation = 2
        if not bonus:
            platforms_speed = 2
            platforms_creation = 60

        # Writing the score
        writer.clear()
        writer.write("Score: " + points.__str__(), align="center", font=("Comic Sans MS", 24, "normal"))

        # Moving Platforms
        for platform in platforms:
            platform.back(platforms_speed)

        for platform in platforms_top:
            platform.back(platforms_speed)

        for cloud in clouds:
            cloud.back()

        if challenge_timer > 700:
            if challenge_clock == 11:
                cur_pos = positions[challenge_counter]
                challenge_counter += counter_direction
                if challenge_counter == 6:
                    counter_direction = -1
                if challenge_counter == 0:
                    counter_direction = 1
                challenge_clock = 0
                platform_bot = turtle.Turtle()
                platform_bot.shape("square")
                platform_bot.shapesize(stretch_wid=cur_pos.get_bot_width(), stretch_len=1)
                platform_bot.color("green")
                platform_bot.penup()
                platform_bot.goto(400, cur_pos.get_bot_y())
                platform2 = turtle.Turtle()
                platform2.shape("square")
                platform2.shapesize(stretch_wid=cur_pos.get_top_width(), stretch_len=1)
                platform2.color("green")
                platform2.penup()
                platform2.goto(400, cur_pos.get_top_y())
                platforms.append(platform_bot)
                platforms_top.append(platform2)
            challenge_clock += 1
            if challenge_timer == 900:
                challenge_timer = 0

        # Creating Platforms
        if timer > platforms_creation and platforms_creation < challenge_timer < 700:
            pos = random.randint(0, len(positions)-1)
            cur_pos = positions[pos]
            timer = 0
            platform_bot = turtle.Turtle()
            platform_bot.shape("square")
            platform_bot.shapesize(stretch_wid=cur_pos.get_bot_width(), stretch_len=1)
            platform_bot.color("green")
            platform_bot.penup()
            platform_bot.goto(400, cur_pos.get_bot_y())
            platform2 = turtle.Turtle()
            platform2.shape("square")
            platform2.shapesize(stretch_wid=cur_pos.get_top_width(), stretch_len=1)
            platform2.color("green")
            platform2.penup()
            platform2.goto(400, cur_pos.get_top_y())
            platforms.append(platform_bot)
            platforms_top.append(platform2)

        # Check if bird is collided on platform
        for platform in platforms:
            if bird.xcor()-10 <= platform.xcor() <= bird.xcor()+20:
                if bird.ycor() < platform.ycor()+(platform.shapesize()[0]*11):
                    #Player disqualification
                    isGameOver = not bonus
                    display_game_over(points)
            if platform.xcor() < -400:
                platforms.remove(platform)
                platform.hideturtle()

            if platform.xcor() == bird.xcor() and bird.ycor() > platform.ycor() + (platform.shapesize()[0] * 11):
                # Player score
                points += 1

        for platform in platforms_top:
            if bird.xcor()-10 <= platform.xcor() <= bird.xcor()+20:
                if bird.ycor() > platform.ycor()-(platform.shapesize()[0]*11):
                    isGameOver = not bonus
                    display_game_over(points)
            if platform.xcor() < -400:
                platforms_top.remove(platform)
                platform.hideturtle()

        bird.shape(bird_gif[gif_frame])
        # Update bird's velocity due to gravity
        bird_velocity_y -= 2

        # Update bird's position
        bird.sety(bird.ycor() + bird_velocity_y)

        # Check if bird hits the ground
        if bird.ycor() < -90:
            bird.sety(-90)
            bird_velocity_y = 0
        if bird.ycor() > 370:
            bird.sety(370)
            bird_velocity_y = 0

        if index > 5:
            gif_frame = 1
        if index > 10:
            gif_frame = 2
        if index > 15:
            gif_frame = 0
            index = 0

        index += 1
        timer += 1
        clouds_timer += 1
        challenge_timer += 1

        if clouds_timer == 80:
            clouds_timer = 0
            clouds.append(Cloud(800, random.randint(50, 330)))

        # Update the screen
        wn.update()

        # Pause for a short time
        sleep(0.02)

    while pause:
        wn.update()
        bird.shape(bird_gif[gif_frame])
        if index > 5:
            gif_frame = 1
        if index > 10:
            gif_frame = 2
        if index > 15:
            gif_frame = 0
            index = 0

        index += 1

time.sleep(5)
