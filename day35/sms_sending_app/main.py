import tkinter as tk
from tkinter import messagebox
from twilio.rest import Client

# ACCOUNT_SID = ''
# AUTH_TOKEN = ''
# TWILIO_PHONE_NUMBER = ''

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Function to send SMS
def send_sms():
    phone_number = phone_entry.get()
    message_body = message_entry.get("1.0", tk.END).strip()

    if not phone_number or not message_body:
        messagebox.showwarning("Input Error", "Please fill in both phone number and message.")
        return

    try:
        # Send SMS using Twilio
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        messagebox.showinfo("Success", f"SMS sent successfully! Message SID: {message.sid}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send SMS: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("SMS Sender App")

# Phone number input
tk.Label(root, text="Phone Number (with country code):").grid(row=0, column=0, padx=10, pady=10)
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=0, column=1, padx=10, pady=10)

# Message input
tk.Label(root, text="Message:").grid(row=1, column=0, padx=10, pady=10)
message_entry = tk.Text(root, width=30, height=5)
message_entry.grid(row=1, column=1, padx=10, pady=10)

# Send button
send_button = tk.Button(root, text="Send SMS", command=send_sms)
send_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the app
root.mainloop()