from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.all_snake = []
        self.create_snake()

    def create_snake(self):
        for position in POSITION:
            self.add_snakes(position)

    def add_snakes(self, position):
        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.all_snake.append(snake)

    def reset(self):
        for snake in self.all_snake:
            snake.goto(1000, 1000)
        self.all_snake.clear()
        self.create_snake()
        self.all_snake[0] = self.all_snake[0]

    def extend(self):
        self.add_snakes(self.all_snake[-1].position())

    def move(self):
        for snake_num in range(len(self.all_snake) - 1, 0, -1):
            new_position_x = self.all_snake[snake_num - 1].xcor()
            new_position_y = self.all_snake[snake_num - 1].ycor()
            self.all_snake[snake_num].goto(new_position_x, new_position_y)
        self.all_snake[0].forward(MOVE_DISTANCE)

    def up_move(self):
        if self.all_snake[0].heading() != 270:
            self.all_snake[0].setheading(90)

    def down_move(self):
        if self.all_snake[0].heading() != 90:
            self.all_snake[0].setheading(270)

    def left_move(self):
        if self.all_snake[0].heading() != 0:
            self.all_snake[0].setheading(180)

    def right_move(self):
        if self.all_snake[0].heading() != 180:
            self.all_snake[0].setheading(0)