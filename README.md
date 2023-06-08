# Simple-Python-Projects-for-Beginners
This are some of the projects i tried as a beginner in python.
These are basic projects for beginners.

#Hangman is a classic word-guessing game.

In this code, the select_word function randomly selects a word from a predefined word list. The display_word function generates a string with the guessed letters and underscores for the unknown letters. The hangman function implements the main logic of the game.

When you run the script, it will prompt you to guess letters to uncover the hidden word. You have six attempts to guess the word correctly. If you guess a correct letter, it will be added to the list of guessed letters and displayed in the word. If you guess an incorrect letter, your attempts will decrease by one. If you run out of attempts, the game ends, and the correct word is revealed.

#Password Generator

In this updated code, we import the tkinter module and use it to create the main window, labels, entry fields, and buttons for the GUI. When the "Generate Password" button is clicked, the generate_button_clicked function is called, which performs the password generation and updates the password entry field with the generated password.

To run the password generator with the GUI, you can execute the script, and a window will appear. Enter the desired password length in the entry field, click the "Generate Password" button, and the generated password will be displayed in the corresponding entry field.

Feel free to customize the GUI further by modifying the appearance, adding additional labels or buttons, or including other features to enhance the user experience.

#To-Do List Manger

 I made corrections to the add_task and delete_task functions.

The add_task function now directly inserts the task into the task listbox using task_listbox.insert(tk.END, task) instead of relying on a separate tasks list. It then clears the entry field using task_entry.delete(0, tk.END). If the entry field is empty when the "Add Task" button is clicked, it displays a warning message using messagebox.showwarning.

The delete_task function retrieves the selected task using task_listbox.curselection() and deletes it from the task listbox using task_listbox.delete(selected_task).

Now, when you enter a task in the entry field and click the "Add Task" button, the task will be directly added to the task listbox. To delete a task, select it in the listbox and click the "Delete Task" button.





