import pandas as pd
import smtplib
import random
import datetime as dt

# Email configuration
MY_EMAIL = 'piyushgilada12@gmail.com'
PASSWORD = 'kpyd gvnj tvli tkvm'  # Use environment variables for security

# File paths
BIRTHDAYS_FILE = '/Users/piyush/python/piyush/pythonProject/day32/birthdays.csv'
LETTER_TEMPLATES_DIR = '/Users/piyush/python/piyush/pythonProject/day32/letter_templates'

# Read the birthdays CSV file
birth_details = pd.read_csv(BIRTHDAYS_FILE)

# Get today's date
now = dt.datetime.now()
today = (now.month, now.day)

# Check if today matches any birthday in the CSV
for index, row in birth_details.iterrows():
    birthday = (row['month'], row['day'])
    if today == birthday:
        # Extract recipient details
        recipient_name = row['name']
        recipient_email = row['email']

        # Pick a random letter template
        letter_template = random.choice(['letter_1.txt', 'letter_2.txt', 'letter_3.txt'])
        with open(f'{LETTER_TEMPLATES_DIR}/{letter_template}', 'r', encoding='utf-8') as file:
            message = file.read()

        # Replace [NAME] with the recipient's name
        personalized_message = message.replace('[NAME]', recipient_name)

        # Send the email
        try:
            with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
                connection.starttls()  # Secure the connection
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=recipient_email,
                    msg=f'Subject: Happy Birthday, {recipient_name}!\n\n{personalized_message}'.encode('utf-8')
                )
            print(f"Birthday email sent to {recipient_name} at {recipient_email} x")
        except smtplib.SMTPException as e:
            print(f"Error sending email to {recipient_email}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")