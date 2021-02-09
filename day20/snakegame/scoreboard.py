from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 26, "normal")

class Scoreboard(Turtle):
    
    def __init__(self, score):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 270)
        self.penup()
        
        self.color("white")
        self.write(f"Score: {score}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update(self, score):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {score}", True, align=ALIGNMENT, font=FONT)
