from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class CarManager():
    
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        create_car = random.randint(1, 6)
        if create_car == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            y_starting_pos = random.randint(-280, 0) # (-280, 230)
            new_car.goto(280, y_starting_pos)
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

    def collision(self):
        sign = Turtle()
        sign.car_speed = 0
        sign.color('black')
        sign.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
