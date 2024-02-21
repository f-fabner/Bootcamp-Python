# f = open("N:\Programando\ProjetosGit\Bootcamp-Python\Days\Day_025\Learning\weather_data.csv", "r")
# print(f.readlines())
# or
# with open("N:\Programando\ProjetosGit\Bootcamp-Python\Days\Day_025\Learning\weather_data.csv") #as data_file:
#    data = data_file.readlines()
#    print(data)
'''
import csv

with open("N:\Programando\ProjetosGit\Bootcamp-Python\Days\Day_025\Learning\weather_data.csv") as data_file:
    data = csv.reader(data_file)
    next(data)
    temperatures = []
    for row in data:
        print(row)
        temperature = int(row[1])
        temperatures.append(temperature)     
    print(temperatures)
'''
import pandas

data = pandas.read_csv(
    "N:\Programando\ProjetosGit\Bootcamp-Python\Days\Day_025\Learning\weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(sum(temp_list) / (len(temp_list)))

# print(data["temp"].max())


# get data in columns
# print(data["condition"]) #lembrar de verificar letras maiúsculas
# print(data.condition)    #lembrar de verificar letras maiúsculas

# get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(monday.temp * (9/5) + 32)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76,  56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
