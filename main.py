import turtle
from states_manager import StateManager
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
    answer_state = screen.textinput(title=f"{correct_states}/50 States Correct",
                                    prompt="What's another States' name?").title()
    if answer_state.title() in states_list:
        states_manager = StateManager()
        correct_states += 1
        state = states_data[states_data.state == answer_state]
        x_cor = state.x.item()
        y_cor = state.y.item()
        states_manager.move(x_cor, y_cor)
        states_manager.show_state(answer_state)

