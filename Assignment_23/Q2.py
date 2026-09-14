# Build a currency converter application that converts between different currencies. The
# user should be able to enter an amount, select the input currency, select the output
# currency, and see the converted amount.

import tkinter as tk
from tkinter import ttk, messagebox

rates = {
    "USD": 1,
    "INR": 83.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 149.0
}


def convert_currency():

    try:
        amount = float(amount_entry.get())

        if amount < 0:
            messagebox.showerror("Error", "Amount cannot be negative")
            return

        from_currency = from_combo.get()
        to_currency = to_combo.get()

        if from_currency == "" or to_currency == "":
            messagebox.showerror("Error", "Please select currencies")
            return

        # Convert to USD first
        usd_amount = amount / rates[from_currency]

        # Convert USD to target currency
        result = usd_amount * rates[to_currency]

        result_label.config(
            text=f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount")


# Create window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x350")


# Title
title_label = tk.Label(
    root,
    text="Currency Converter",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)


# Amount
amount_label = tk.Label(root, text="Enter Amount:")
amount_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)


# From Currency
from_label = tk.Label(root, text="From Currency:")
from_label.pack(pady=5)

from_combo = ttk.Combobox(
    root,
    values=["USD", "INR", "EUR", "GBP", "JPY"],
    state="readonly"
)
from_combo.pack()


# To Currency
to_label = tk.Label(root, text="To Currency:")
to_label.pack(pady=5)

to_combo = ttk.Combobox(
    root,
    values=["USD", "INR", "EUR", "GBP", "JPY"],
    state="readonly"
)
to_combo.pack()


# Convert button
convert_button = tk.Button(
    root,
    text="Convert",
    command=convert_currency
)
convert_button.pack(pady=20)


# Result
result_label = tk.Label(
    root,
    text="Converted amount will appear here",
    font=("Arial", 12, "bold")
)
result_label.pack(pady=10)


# Run application
root.mainloop()