from turtle import Turtle
from pygame import mixer

FONT = ("Ariel", 18, "normal")
ALIGNMENT = "center"

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    #If the user loses the game
    def lose_game(self):
        self.goto(0, 0)
        mixer.music.load(r'game_over_sound.mp3')
        mixer.music.play()
        self.write("YOU LOST....", align=ALIGNMENT, font=FONT)

    # If the user wins the game
    def win_game(self):
        self.goto(0, 0)
        mixer.music.load(r'game_win_sound.mp3')
        mixer.music.play()
        self.write("YOU WON !!!", align=ALIGNMENT, font=FONT)

    #If the turtle color mentioned by the user does not exist
    def player_not_found(self):
        self.goto(0, 0)
        mixer.music.load(r'game_error_sound.mp3')
        mixer.music.play()
        self.write("PLAYER NOT FOUND\n\n......TRY AGAIN......", align=ALIGNMENT, font=FONT)
