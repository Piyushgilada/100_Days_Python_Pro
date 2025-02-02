import turtle,pandas as pd

import pandas

screen=turtle.Screen()
screen.title("U.S States Game")
screen.addshape('/Users/piyush/python/piyush/pythonProject/day25B/blank_states_img.gif')
turtle.shape('/Users/piyush/python/piyush/pythonProject/day25B/blank_states_img.gif')


guessed_state=[]
data=pd.read_csv('/Users/piyush/python/piyush/pythonProject/day25B/50_states.csv')
all_state=data.state.to_list()
while len(guessed_state) < 50:
    user_input = screen.textinput(f'{len(guessed_state)}/50 states Guessed', 'Please Guess ').title()
    if user_input=="Exit":
        missing_state=[state for state in all_state if state not in guessed_state]  # list comprehension
        new_data=(pandas.DataFrame(missing_state))
        new_data.to_csv('/Users/piyush/python/piyush/pythonProject/day25B/missing_state.csv')
        break
    if user_input in all_state:
        guessed_state.append(user_input)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state == user_input]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(user_input)
# def On_mouse_click(x,y):
#     print(x,y)
# turtle.onscreenclick(On_mouse_click)
turtle.mainloop()
screen.exitonclick()