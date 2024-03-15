import datetime as dt
import smtplib
import random


with open("N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_032/quotes_ptbr.txt") as data:
    quotes = data.readlines()

quotes = [quote.strip() for quote in quotes]

random_quote = random.choice(quotes)

# substituir pelo gmail que vc quer utilizar pra enviar
my_email = "xxxxxx@gmail.com"
password = "xxxxxxxxxxx"  # substituir peloa senha app que o gmail enviar
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

# date_of_birth = dt.datetime(year=1990, month=3, day=22, hour=4)
# print(date_of_birth)
if day_of_week == 4:
    with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        # substituir o email abaixo pelo destinatário que vc quer enviarpelo gmail que vc quer utilizar pra enviar
        connection.sendmail(from_addr=my_email, to_addrs="xxxxxxxxxx@gmail.com",
                            msg=f"Subject: Citação do Dia:\n\n{random_quote}")
        connection.close
