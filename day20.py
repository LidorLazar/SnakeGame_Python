from turtle import Screen
from classSnake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.onkey(snake.up_move, 'Up')
screen.onkey(snake.down_move, 'Down')
screen.onkey(snake.left_move, 'Left')
screen.onkey(snake.right_move, 'Right')

game_is_on = True


while game_is_on:
    # move snake
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.all_snake[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.all_snake[0].xcor() > 290 or snake.all_snake[0].xcor() < -290 or snake.all_snake[0].ycor() > 290 or snake.all_snake[0].ycor() < -290:
        scoreboard.reset()
        snake.reset()
    # # Detect collision with tail
    for one_snake in snake.all_snake:
        if one_snake == snake.all_snake[0]:
            pass
        elif snake.all_snake[0].distance(one_snake) < 10:
            scoreboard.reset()
            snake.reset()



    # if head collision with any sigment in the tail:





screen.exitonclick()