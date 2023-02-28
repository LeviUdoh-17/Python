# with open("100days/day_25/weather_data.csv", "r") as file:
#     data = file.readlines()
#     print(data)

# import csv
# with open("100days/day_25/weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

# import pandas

# data = pandas.read_csv("100days/day_25/weather_data.csv")
# print(data["temp"])
import pandas

# Black, Gray, Cinnamon = 0, 0, 0
data = pandas.read_csv("100days/day_25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# for color in data["Primary Fur Color"]:
#     if color == "Black":
#         Black += 1
#     if color == "Gray":
#         Gray += 1
#     if color == "Cinnamon":
#         Cinnamon += 1
Black = len(data[data["Primary Fur Color"] == "Black"])
Gray = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

new_data = pandas.DataFrame({
    "Fur Color" : ["Gray", "Red", "Black"], 
    "Count" : [f"{Gray}", f"{Cinnamon}", f"{Black}"]
})
new_data.to_csv("100days/day_25/new_data.csv")