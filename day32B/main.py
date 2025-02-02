import random
import smtplib
import datetime as dt

# Email configuration
MY_EMAIL = 'piyushgilada12@gmail.com'
PASSWORD = 'kpyd gvnj tvli tkvm'  # Use environment variables for security
RECIPIENT_EMAIL = 'piyushgilada.skn.it@gmail.com'

# File path to quotes
QUOTES_FILE = '/day32B/quotes.txt'

# Get current date and time
now = dt.datetime.now()
weekday = now.weekday()

# Check if today is Thursday (weekday == 3)
if weekday == 3:
    try:
        # Read quotes from file
        with open(QUOTES_FILE, 'r', encoding='utf-8') as file:
            quotes = file.readlines()

        # Select a random quote
        message = random.choice(quotes).strip()  # Remove extra newlines
        print (message)
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECIPIENT_EMAIL,
                msg=f'Subject: Motivation for Thursday!\n\n{message}'.encode('utf-8')
            )
        print("Email sent successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{QUOTES_FILE}' was not found.")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
else:
    print("Today is not Thursday. No email sent.")