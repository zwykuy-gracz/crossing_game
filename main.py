import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move_cars()

    if player.ycor() > -240:
        player.reset_position()
        scoreboard.point()
        carmanager.speed_up()

    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            carmanager.collision()

