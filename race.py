from turtle import Turtle, Screen
import random

is_race = False

screen = Screen()
screen.setup(500, 400)
colo = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
user_bet = screen.textinput(title="make your bet", prompt="enter a color")
print(user_bet)
y_position = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    new_turtle.color(colo[turtle_index])
    all_turtle.append(new_turtle)
if user_bet:
    is_race = True
while is_race:
      for turtle in all_turtle:
          if turtle.xcor()>230 :
              is_race=False
              winner=turtle.pencolor()
              if winner==user_bet:
                  print(f"congratulation you {winner}won")
              else:
                  print(f"you lost brother you lost brother couz the winner is {winner}")


          random_distance = random.randint(0, 10)
          turtle.forward(random_distance)

screen.exitonclick()
