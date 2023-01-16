# import turtle
# timmy = turtle.Turtle()
# my_screen = turtle.Screen()
# print(timmy)
# timmy.color("coral")
# timmy.shape("turtle")
# timmy.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align["Pokemon Name"] = "l"
table.align["Type"] = "l"
print(table)
