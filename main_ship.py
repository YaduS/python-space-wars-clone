from turtle import _Screen, Turtle
from game_constants import MAX_Y, MIN_X, MAX_X
from typing import List

STARTING_POSITION = (0, -240)
MOVE_SPEED = 15
PROJECTILE_SPEED = 5
SHIP_MAX_HEALTH = 30
HIT_DAMAGE = (
    3  # makes more sense to be a property of the projectile(enemy's in this case)
)


class MainShip(Turtle):

    def __init__(self, screen: _Screen):
        super().__init__()
        self.set_shape(screen)
        self.configure_listeners(screen)
        self.projectiles: List[Turtle] = []
        self.MAX_HEALTH = SHIP_MAX_HEALTH
        self.current_health = SHIP_MAX_HEALTH

    def set_shape(self, screen: _Screen):
        self.penup()
        self.setposition(STARTING_POSITION)
        self.shape("./spaceship.gif")
        self.resizemode("user")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=0)

    def configure_listeners(self, screen: _Screen):
        # keys to move left
        for key in ["Left", "a", "A"]:
            screen.onkeypress(
                fun=self.move_left,
                key=key,
            )

        # keys to move right
        for key in ["Right", "d", "D"]:
            screen.onkeypress(
                fun=self.move_right,
                key=key,
            )

        # key to fire
        screen.onkeypress(fun=self.fire, key="space")

        screen.onkeypress(fun=lambda: screen.bye(), key="Escape")
        screen.listen()

    def move_left(self):
        xcor = self.xcor()
        if xcor > MIN_X - 10:
            self.goto(x=xcor - MOVE_SPEED, y=self.ycor())

    def move_right(self):
        xcor = self.xcor()
        if xcor < MAX_X - 10:
            self.goto(x=xcor + MOVE_SPEED, y=self.ycor())

    def create_projectile(self):
        rocket = Turtle(shape="square")
        rocket.penup()
        rocket.setposition((self.xcor(), self.ycor() + 20))
        rocket.color("green")
        rocket.resizemode("user")
        rocket.shapesize(stretch_wid=0.5, stretch_len=0.1, outline=0)
        self.projectiles.append(rocket)

    def move_existing_projectiles(self):
        projectiles_to_remove = []
        for i, projectile in enumerate(self.projectiles):
            ycor = (
                projectile.ycor() + PROJECTILE_SPEED
                if projectile.ycor() < MAX_Y
                else projectile.ycor()
            )
            if ycor >= MAX_Y:
                projectiles_to_remove.append(i)
            else:
                projectile.goto(x=projectile.xcor(), y=ycor)

        for index in projectiles_to_remove[::-1]:
            print("index: ", index)
            self.projectiles[index].clear()
            self.projectiles[index].hideturtle()
            del self.projectiles[index]

    def fire(self):
        self.create_projectile()

    def cycle_update(self):
        self.move_existing_projectiles()

    def ship_hit(self):
        if self.current_health > 0:
            self.current_health -= HIT_DAMAGE
        print(f"ship hit; current health: {self.current_health}")
