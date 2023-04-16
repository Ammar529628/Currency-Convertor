import tkinter as tk
from tkinter import ttk

class CurrencyConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Ammar Currency Converter")

        # Define conversion rates for currencies
        self.conversion_rates = {
            "USD": {"EUR": 0.83, "JPY": 110.0, "GBP": 0.75, "PKR": 260.0},
            "EUR": {"USD": 1.2, "JPY": 132.0, "GBP": 0.9, "PKR": 313.25},
            "JPY": {"USD": 0.009, "EUR": 0.0076, "GBP": 0.0068, "PKR": 2.36},
            "GBP": {"USD": 1.33, "EUR": 1.11, "JPY": 146.0, "PKR": 346.67},
            "PKR": {"USD": 0.0038, "EUR": 0.0032, "JPY": 0.4245, "GBP": 0.0029}
        }

        # Create currency selection dropdowns
        currencies = ["USD", "EUR", "JPY", "GBP", "PKR"]
        self.from_currency = tk.StringVar(value=currencies[0])
        self.to_currency = tk.StringVar(value=currencies[1])
        from_currency_menu = ttk.OptionMenu(master, self.from_currency, *currencies)
        to_currency_menu = ttk.OptionMenu(master, self.to_currency, *currencies)
        from_currency_menu.grid(row=0, column=0, padx=10, pady=10)
        to_currency_menu.grid(row=0, column=2, padx=10, pady=10)

        # Create input fields for amount
        self.from_amount = tk.DoubleVar()
        self.to_amount = tk.DoubleVar()
        from_amount_entry = ttk.Entry(master, textvariable=self.from_amount)
        to_amount_entry = ttk.Entry(master, textvariable=self.to_amount, state="readonly")
        from_amount_entry.grid(row=1, column=0, padx=10, pady=10)
        to_amount_entry.grid(row=1, column=2, padx=10, pady=10)

        # Create button for conversion
        convert_button = ttk.Button(master, text="Convert", command=self.convert)
        convert_button.grid(row=1, column=1, padx=10, pady=10)

        # Create button for reset
        reset_button = ttk.Button(master, text="Reset", command=self.reset)
        reset_button.grid(row=2, column=1, padx=10, pady=10)

    def convert(self):
        try:
            # Get amount to convert from input field
            from_amount = self.from_amount.get()
            from_currency = self.from_currency.get()
            to_currency = self.to_currency.get()

            # Convert based on conversion rates
            to_amount = from_amount * self.conversion_rates[from_currency][to_currency]

            # Update output field with converted amount
            self.to_amount.set(round(to_amount, 2))
        except ValueError:
            # Handle invalid input
            self.to_amount.set("Invalid input")

    def reset(self):
        # Clear input and output fields
        self.from_amount.set(0)
        self.to_amount.set(0)

root = tk.Tk()
app = CurrencyConverter(root)
root.mainloop()