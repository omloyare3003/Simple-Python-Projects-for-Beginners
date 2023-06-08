import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

# Create the main window
window = tk.Tk()
window.title("To-Do List Manager")

# Create and place the widgets
task_entry = tk.Entry(window, width=50)
task_entry.pack()

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack()

task_listbox = tk.Listbox(window, width=50)
task_listbox.pack()

# Start the GUI main loop
window.mainloop()
