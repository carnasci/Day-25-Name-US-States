import turtle
from turtle import Turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


states_data = pandas.read_csv("50_states.csv")
states = states_data.state
states_list = states.to_list()

correct_states = 0

# ohio = states_data[states_data.state == "Ohio"]
# print(ohio.x)

while correct_states < 50:
    answer_state = screen.textinput(title=f"{correct_states}/50 States Correct", prompt="What's another States' name?")
    if answer_state.title() in states_list:
        correct_states += 1
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.write(f"{answer_state.title()}", align="center", font=("Courrier", 12, "normal"))

        state = states_data[states_data.state == f"{answer_state.title()}"]
        x_cor = int(state.x)
        y_cor = int(state.y)
        print(x_cor)
        print(y_cor)

        new_turtle.goto(x_cor, y_cor)
