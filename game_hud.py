# for game hud components like score, ship healthy, level etc.?

from turtle import Turtle
from game_constants import HEALTH_BAR_HEIGHT, HEALTH_BAR_WIDTH, HEALTH_BAR_POS
from main_ship import SHIP_MAX_HEALTH


class GameHUD:

    def __init__(self):
        self.create_hud_elements()

    def create_hud_elements(self):
        self.draw_health_bar(SHIP_MAX_HEALTH, SHIP_MAX_HEALTH)

    def draw_health_bar(self, current_health: int, max_health: int):
        t = Turtle()
        t.hideturtle()
        t.penup()

        # draw outline
        t.goto((HEALTH_BAR_POS[0] - 1, HEALTH_BAR_POS[1] - 1))
        t.color("yellow")
        t.left(90)
        t.pendown()
        for i in range(2):
            t.forward(HEALTH_BAR_HEIGHT + 2)
            t.right(90)
            t.forward(HEALTH_BAR_WIDTH + 1)
            t.right(90)
        t.penup()

        # fill health
        t.goto(HEALTH_BAR_POS)
        t.color("green")
        t.begin_fill()
        for _ in range(2):
            t.forward(HEALTH_BAR_HEIGHT)
            t.right(90)
            t.forward(HEALTH_BAR_WIDTH)
            t.right(90)
        t.end_fill()

    def create_score_board(self):
        pass
