import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Bag")

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("No task selected", "Please select a task to remove.")

def mark_completed():
    selected_task = listbox.curselection()
    if selected_task:
        task = listbox.get(selected_task)
        listbox.itemconfig(selected_task, {'bg': 'light green', 'selectbackground': 'light green'})
        messagebox.showinfo("Task added", f"{task} marked as completed!")
    else:
        messagebox.showwarning("No Item Selected", "Please select an item to mark as completed.")

# Create the main window
root = tk.Tk()
root.title("To Do Task App")

# Entry widget for adding tasks
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, padx=10, pady=10)

# Button to add a task
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=10)

# Listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=30)
listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Button to remove a task
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.grid(row=2, column=0, pady=5)

# Button to mark a task as completed
complete_button = tk.Button(root, text="Task Completed", command=mark_completed)
complete_button.grid(row=2, column=1, pady=5)

# Run the Tkinter event loop
root.mainloop()# Write your code here :-)
# Write your code here :-)
