import datetime as dt
import smtplib
import random
import pandas as pd
import os

birthdays = pd.read_csv("N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_032/Birthday/birthdays.csv")

my_email = "xxxxxx@gmail.com"
password = "xxxxxxxxxxx"
now = dt.datetime.now()
year = now.year
month = now.month
today_day = now.day

is_birthday = birthdays[(birthdays['month'] == month) & (birthdays['day'] == today_day)]

if not is_birthday.empty:
    letter_directory = "N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_032/Birthday/letter_templates"
    letter_files = os.listdir(letter_directory)
    letter_choice = random.choice(letter_files)


    with open(f"N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_032/Birthday/letter_templates/{letter_choice}") as letter_file:
        letter_content = letter_file.read()
        
    person_name = is_birthday['name'].values[0]
    letter_content = letter_content.replace("[NAME]", person_name)

    with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="xxxxxxxxxx@gmail.com",
                            msg=f"Subject: Feliz Aniversário!\n\n{letter_content}")
