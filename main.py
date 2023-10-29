from turtle import Turtle, Screen
from gameover import GameOver
import random
from pygame import mixer

mixer.init()
gameobj = GameOver()
my_screen = Screen()

my_screen.title("TURTLE RACE")
my_screen.bgpic("finishline.png")
my_screen.setup(width=1000, height=800)

color_list = ["red", "green", "blue", "orange", "pink", "black"]
y_pos = [-360, -225, -75, 75, 225, 370]
turtles_in_race = []

for i in range(6):
    turtleObj = Turtle("turtle")
    turtleObj.penup()
    turtleObj.shapesize(2.5)
    turtleObj.color(color_list[i])
    turtleObj.goto(x=-472, y=y_pos[i])
    turtles_in_race.append(turtleObj)

mixer.music.load(r'game_start_sound.mp3')
mixer.music.play()
is_race_on = False
user_bet = my_screen.textinput(title="Make your bet", prompt="Which color turtle will win the game?: ")

if user_bet not in color_list:
    # If user bet does not exist then display
    error = gameobj.player_not_found()
else:
    # If user bet exists then perform
    mixer.music.load(r'game_process_sound.mp3')
    mixer.music.play()
    is_race_on = True

while is_race_on:
    for turt in turtles_in_race:
        if turt.xcor() > 430:
            # Checks if x coordinate is >430
            is_race_on = False
            winning_turtle = turt.pencolor()
            if winning_turtle == user_bet:
                print(f"\n\nYou won!!\n{winning_turtle} turtle won the race.")
                gameobj.win_game()
            else:
                print(f"\n\nYou lost!!\n{winning_turtle} turtle won the race.")
                gameobj.lose_game()
        random_dist = random.randint(0, 10)
        turt.forward(random_dist)

my_screen.exitonclick()
