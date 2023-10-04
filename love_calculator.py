import tkinter as tk
from random import randint

# Function to calculate love score
def calculate_love_score():
    name1 = entry_name1.get().strip().lower()
    name2 = entry_name2.get().strip().lower()

    # A simple algorithm for calculating the love score
    love_score = randint(1, 100)

    result_label.config(text=f"Love Score: {love_score}%")

# Create a tkinter window
window = tk.Tk()
window.title("Love Calculator")
window.geometry("400x300")  # Set the window size

# Set the background color to red
window.configure(bg="red")

# Labels
label_name1 = tk.Label(window, text="Enter Name 1:", bg="red", fg="white")
label_name2 = tk.Label(window, text="Enter Name 2:", bg="red", fg="white")
result_label = tk.Label(window, text="", font=("Helvetica", 16), bg="red", fg="white")

# Entry fields
entry_name1 = tk.Entry(window)
entry_name2 = tk.Entry(window)

# Calculate button
calculate_button = tk.Button(window, text="Calculate Love Score", command=calculate_love_score, bg="red", fg="white")

# Pack widgets
label_name1.pack()
entry_name1.pack()
label_name2.pack()
entry_name2.pack()
calculate_button.pack()
result_label.pack()

# Run the tkinter main loop
window.mainloop()
