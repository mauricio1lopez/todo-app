import csv

with open("files/weather.csv") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")
for i in data[1:]:
    if i[0] == city:
        print(i[1])