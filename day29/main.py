import random
import string
from tkinter import messagebox
import json
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"
    pass_letter = random.choices(letters, k=8)
    pass_number = random.choices(numbers, k=4)
    pass_symbol = random.choices(symbols, k=2)
    all_char = pass_number + pass_symbol + pass_letter
    random.shuffle(all_char)
    password = ''.join(all_char)
    password_entry.delete(0, END)  # Clear any existing text in the entry
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()  # Get the website entered by the user
    email = email_entry.get()      # Get the email/username entered by the user
    password = password_entry.get()
    # New data to save
    new_data = {
        website: {'email': email,'password': password}
    }
    # Validate input fields
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please make sure no fields are empty!")
        return
    try:
        # Try to read the existing data
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is empty, initialize with new data
        data = new_data
    else:
        # Update existing data with the new entry
        data.update(new_data)
    # Save the updated data back to the file
    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)
    # Clear the fields after saving
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    messagebox.showinfo(title="Saved", message="Password saved successfully!")

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()  # Get the website entered by the user
    if len(website) == 0:
        messagebox.showwarning(title="Oops", message="Please enter a website to search!")
        return
    try:
        # Try to read the data file
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found!")
    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="Data file is corrupted!")
    else:
        # Check if the website exists in the data
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No details for {website} exist.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, width=200, height=200, bg='white')
logo = PhotoImage(file='logo.png',)
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website", fg='black', bg='white')
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username", fg='black', bg='white')
email_label.grid(row=2, column=0)
password_label = Label(text="Password", fg='black', bg='white')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21, bg='white', fg='black', insertbackground='black', highlightthickness=0, border=1)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35, bg='white', fg='black', insertbackground='black', highlightthickness=0, border=1)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21, fg='black', bg='white', insertbackground='black', highlightthickness=0, border=1)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text='Search', command=search_password, bg='white', width=13)
search_button.grid(row=1, column=2)
generate_password = Button(text='Generate Password', command=password_generator, bg='white')
generate_password.grid(row=3, column=2)
add_button = Button(text='Add', width=36, command=save_password, bg='white')
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
