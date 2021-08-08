# import smtplib

# # --- Gmail starting
# with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
#     connection.starttls()
#     connection.login(user=GMAIL_USERNAME, password=GMAIL_PASSWORD)
#     connection.sendmail(from_addr=GMAIL_USERNAME, to_addrs=GMAIL_USERNAME, msg='Subject:Hello\n\n Hi this is the body')


# --- Yahoo starting
# with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
#     connection.starttls()
#     connection.login(user=YAHOO_USERNAME, password=YAHOO_PASSWORD)
#     connection.sendmail(from_addr=YAHOO_USERNAME, to_addrs=GMAIL_USERNAME, msg='Hello')
#

# import datetime as dt
#
# date_time = dt.datetime.now()
# year = date_time.year
# month = date_time.month
# day = date_time.day
# day_of_week = date_time.now()
# custom_date = dt.datetime(year=1993, month=12, day=19)
# print(date_time)

# import smtplib
# import datetime as dt
# import random
#
#
# current_date = dt.datetime.now()
# if current_date.weekday() == 6:
#     with open('./quotes.txt', 'r') as file:
#         quotes_list = file.readlines()
#         quote = random.choice(quotes_list)
#     with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
#         connection.starttls()
#         connection.login(user=GMAIL_USERNAME, password=GMAIL_PASSWORD)
#         connection.sendmail(
#             from_addr=GMAIL_USERNAME,
#             to_addrs=GMAIL_USERNAME,
#             msg=f'Subject: Happy Sunday\n\n{quote}')

"""

This script checks a csv that contains a persons name and birthday
against the current date. If it is a persons birthday, an email is sent
congratulating them.

This script requires that 'smtplib', 'pandas', and 'python-dotenv' be installed within the Python
environment you are running this script in.

"""

import smtplib
import datetime as dt
import random
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv('.env')
GMAIL_USERNAME = os.getenv("GMAIL_USERNAME")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
YAHOO_USERNAME = os.getenv("YAHOO_USERNAME")
YAHOO_PASSWORD = os.getenv("YAHOO_PASSWORD")
LETTERS_FILE_LIST = ['./letter_templates/letter_1.txt', './letter_templates/letter_2.txt', './letter_templates/letter_3.txt']


def check_birthday(row):

    current_date = dt.datetime.now()
    if row['month'] == current_date.month and row['day'] == current_date.day:
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=GMAIL_USERNAME, password=GMAIL_PASSWORD)
            letter_file = random.choice(LETTERS_FILE_LIST)
            with open(letter_file, 'r') as file:
                message = file.read()
                message = message.replace('[NAME]', row['name'])
                connection.sendmail(from_addr=GMAIL_USERNAME, to_addrs=row['email'], msg=f'Subject:HAPPY BIRTHDAY!\n\n{message}')

df = pd.read_csv('./birthdays.csv')
df.apply(func=check_birthday, axis=1)

