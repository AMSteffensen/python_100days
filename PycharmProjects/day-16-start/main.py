#from turtle import *

#timmy = Turtle()
#print(timmy)
#timmy.shape("turtle")
#timmy.color("DarkGreen")
#my_screen = Screen()
#print(my_screen.canvheight)

#while True:
#    forward(200)
#    left(170)
#my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable([])
table.add_column("Pokemon name", ["Pikachu", "Squritle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align["Pokemon name"] = "c"

print(table)