from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_score()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Ariel", 24, "normal"))

    def reset(self):
        if self.score > int(self.high_score):
            new_high_score = self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(new_high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def read_score(self):
        with open("data.txt") as file:
            new_score = file.read()
        return new_score

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=("Ariel", 24, "normal"))