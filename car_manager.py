from random import choice , randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.car_list = []
        self.create_cars()
        self.increment = 0

    def create_cars(self):
        for i in range (31):
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.goto( x = randint(170 , 840) , y = randint(-250 , 250) )
            self.car_list.append(new_car)


    def move_cars(self):
        for car in self.car_list:
                car.fd(STARTING_MOVE_DISTANCE + self.increment)
                if car.xcor() < -300:
                    car.goto(x=randint(270, 550), y=randint(-250, 250))


    def increase_speed(self):
        self.increment += MOVE_INCREMENT

















# Step - 2:
# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen.
# No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle).
# Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video walkthrough in Step 4.