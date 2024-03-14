'''
import smtplib

my_email = "xxxxxx@gmail.com"#substituir pelo gmail que vc quer utilizar pra enviar
password = "xxxxxxxxxxx"#substituir peloa senha app que o gmail enviar


with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    #substituir o email abaixo pelo destinatário que vc quer enviarpelo gmail que vc quer utilizar pra enviar
    connection.sendmail(from_addr=my_email, to_addrs="xxxxxxxxxx@gmail.com", msg="Subject:hello\n\nThis is the body of my email... Hello")
    connection.close
'''
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1990, month=3, day=22, hour=4)
print(date_of_birth)