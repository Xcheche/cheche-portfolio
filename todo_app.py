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
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete.")

def edit_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        selected_task = task_listbox.get(selected_task_index)
        task_entry.delete(0, tk.END)  # Clear the entry field
        task_entry.insert(0, selected_task)  # Pre-fill the entry field with the selected task
        task_listbox.delete(selected_task_index)  # Remove the selected task from the list
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to edit.")

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
            for task in tasks:
                task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List App")

# Create a listbox to display tasks
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, bg="#f2f2f2")
task_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Create an entry field to add/edit tasks
task_entry = tk.Entry(root, font=("Helvetica", 14))
task_entry.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

# Create buttons for adding, editing, deleting, and saving tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
edit_button = tk.Button(root, text="Edit Task", command=edit_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
save_button = tk.Button(root, text="Save Tasks", command=save_tasks)

add_button.pack(pady=5, padx=10, fill=tk.BOTH)
edit_button.pack(pady=5, padx=10, fill=tk.BOTH)
delete_button.pack(pady=5, padx=10, fill=tk.BOTH)
save_button.pack(pady=5, padx=10, fill=tk.BOTH)

# Load saved tasks (if any)
load_tasks()

# Start the Tkinter main loop
root.mainloop()
