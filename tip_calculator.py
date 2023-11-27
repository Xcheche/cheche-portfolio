import tkinter as tk
from tkinter import PhotoImage


def calculate_tip():
    bill = float(entry_bill.get())
    tip_percentage = int(entry_tip.get())
    people = int(entry_people.get())

    tip_as_percent = tip_percentage / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)

    result_label.config(text=f'Each person should pay: ${final_amount}')


# Create main window
app = tk.Tk()
app.title('Tip Calculator')
app.resizable(0, 0)
app.config(bg='lightgrey')

# Set app icon
# Replace 'path_to_icon.png' with your icon file path
# icon_photo = PhotoImage(file='images/tip-calculator.png')
# icon_photo = icon_photo.subsample(2)
# app.iconphoto(False, icon_photo)

# Create and set up widgets
label_bill = tk.Label(app, text='What was the total bill ? $')
entry_bill = tk.Entry(app)

label_tip = tk.Label(
    app, text='How much tip would you like to give? 10, 12, or 15 ?')
entry_tip = tk.Entry(app)

label_people = tk.Label(app, text='How many people to split the bill ?')
entry_people = tk.Entry(app)

calculate_button = tk.Button(
    app, text='Calculate', bg='blue', fg='white', command=calculate_tip)

result_label = tk.Label(app, bg='white', text='')

exit_button = tk.Button(app, text='Exit', bg='blue',
                        fg='white', command=app.destroy)

# Place widgets on the grid
label_bill.grid(row=0, column=0)
entry_bill.grid(row=0, column=1)

label_tip.grid(row=1, column=0)
entry_tip.grid(row=1, column=1)

label_people.grid(row=2, column=0)
entry_people.grid(row=2, column=1)

calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label.grid(row=4, column=0, columnspan=2)

exit_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the main loop
app.mainloop()
