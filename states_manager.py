from turtle import Turtle

class StateManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def show_state(self, state):
        self.clear()
        self.write(f"{state}", align="center", font=("Courrier", 12, "normal"))

    def move(self, x_cord, y_cord):
        self.goto(x_cord, y_cord)


