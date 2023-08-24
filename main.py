import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S States Game")
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
df=pandas.read_csv("50_states.csv")
all_states=df['state'].to_list()
guessed_states=[]

while len(guessed_states)<50:
     answer_state=screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="What's another state name?")

     guess=answer_state.title()
     if guess=="Exit":
          missing_states = [state for state in all_states if state not in guessed_states]
          newdf=pandas.DataFrame(missing_states)
          newdf.to_csv("states_to_learn.csv")
          break
     if guess in all_states:
          guessed_states.append(answer_state)
          t= turtle.Turtle()
          t.hideturtle()
          t.penup()
          state_data=df[guess==df.state]
          t.goto(int(state_data.x.iloc[0]),int(state_data.y.iloc[0]))
          t.write(guess)



