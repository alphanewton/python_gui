import pandas
import turtle

screen = turtle.Screen()
screen.title("Guess the U.S states")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()
t.hideturtle()
t.penup()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [states for states in all_states if states not in guessed_states]
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        correct_answer = data[data.state == answer_state]
        t.goto(int(correct_answer.x), int(correct_answer.y))
        t.write(correct_answer.state.item())



screen.exitonclick()