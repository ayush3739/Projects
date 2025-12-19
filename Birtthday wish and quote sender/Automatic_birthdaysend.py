##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import datetime as dt
import smtplib
import random

my_email="Your email-here"
passw="Your password"


data=pd.read_csv('birthdays.csv')


birthdays_dict = {
    (row["month"], row["day"]): row for (index, row) in data.iterrows()
}

now=dt.datetime.now()
day=now.day
month=now.month
weekday=now.isoweekday()


if (month,day) in birthdays_dict:
    birthday_person = birthdays_dict[(month, day)]
    birthday_email = birthday_person["email"]  
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        contents=file.read()
        contents=contents.replace('[NAME]',birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()
        connection.login(user=my_email,password=passw)

        connection.sendmail(
            from_addr=my_email, 
            to_addrs=birthday_email,
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )


with open("quotes.txt","r") as file:
    all_quotes=file.readlines()
    quote=random.choice(all_quotes)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()

    connection.login(user=my_email,password=passw)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=data.email,
        msg=f"subject:Quote of the day\n\n{quote}"
    )

