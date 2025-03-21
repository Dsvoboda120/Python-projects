from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 265)
        self.color("White")
        self.hideturtle()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.clear()
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
    #     self.goto(0, -30)
    #     self.write(f"Your final score is {self.score}.", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()