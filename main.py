# Importing all the required modules
from turtle import Turtle, Screen
import pandas as pd

# Creating objects from the classes
turtle = Turtle()
screen = Screen()

# Setting up screen and adding an image
screen.title("India & States")
image = "India.gif"
screen.addshape(image)
turtle.shape(image)

# Reading csv file which consists of Indian States and their screen co-ordinates
data = pd.read_csv("India_states.csv")
states = data.States.to_list()

guessed_states = []

while len(guessed_states) < 36:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/36 States/UT Correct",
                                    prompt="What's another state/UT's name?").title()
    if answer_state == 'Exit':
        # If the user types in exit, the quiz will end and the program creates a new csv file which contains all the unanswered states 
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missing_locations.csv")
        break
    
    if answer_state in states:
        guessed_states.append(answer_state)
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        state_data = data[data.States == answer_state]
        new_turtle.goto(int(state_data.x), int(state_data.y))
        new_turtle.write(answer_state)

screen.exitonclick()
