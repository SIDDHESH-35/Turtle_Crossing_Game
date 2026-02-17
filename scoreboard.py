FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.update_level()



    def update_level(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", True ,align='left' ,font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER ", False, align='center', font=FONT)