# import michael_tumuhaise_day4_afternoon
# michael_tumuhaise_day4_afternoon.product(3, 3)

import tkinter as tk
from tkinter import messagebox, Entry


def generate_receipt():
    item = item_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()

    # Input validation
    # Will show a message box if there is an error in the input fields
    if not item or not quantity or not price:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    #  Try and Except to catch the errors if any
    try:
        quantity = int(quantity)
        price = float(price)
    except ValueError:
        messagebox.showerror("Error", "Invalid quantity or price.")
        return

    total = quantity * price

    receipt_text = f"Item Brought: {item}\nQuantity Of Item: {quantity}\nPrice Of Item: Ugx{price:.1f}\nTotal Amount: Ugx{total:.1f}"
    receipt_label.config(text=receipt_text)

# Create the main window
window = tk.Tk()
window.title("Michaels Receipt ")

# Create labels and entry fields for input
item_label = tk.Label(window, text="Enter Item Brought:")
item_label.pack()

item_entry = tk.Entry(window)
item_entry.pack()

quantity_label = tk.Label(window, text="Enter Quantity Of Item:")
quantity_label.pack()

quantity_entry: Entry = tk.Entry(window)
quantity_entry.pack()

price_label = tk.Label(window, text="Emter Price Of Item:")
price_label.pack()

price_entry = tk.Entry(window)
price_entry.pack()

# Create a button to generate the receipt
generate_button = tk.Button(window, text="Print Receipt", command=generate_receipt)
generate_button.pack()

# Create a label to display the receipt
receipt_label = tk.Label(window, text="")
receipt_label.pack()

# Run the main event loop
window.mainloop()
