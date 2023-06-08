import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Length should be a positive integer.")
        else:
            password = generate_password(length)
            password_entry.delete(0, tk.END)
            password_entry.insert(tk.END, password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a positive integer.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create and place the widgets
length_label = tk.Label(window, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_button_clicked)
generate_button.pack()

password_label = tk.Label(window, text="Generated Password:")
password_label.pack()

password_entry = tk.Entry(window)
password_entry.pack()

# Start the GUI main loop
window.mainloop()
