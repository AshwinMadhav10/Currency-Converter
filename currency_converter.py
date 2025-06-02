import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# Currency Converter Logic
class CurrencyConverter:
    rates = {
        'USD': 1.00,
        'EUR': 0.92,
        'INR': 82.01,
        'GBP': 0.77,
        'AUD': 1.46,
        'CAD': 1.36,
        'JPY': 156.45,
        'CHF': 0.91
    }

    def convert(self, from_currency, to_currency, amount):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.rates or to_currency not in self.rates:
            messagebox.showerror("Invalid Currency", "Please select valid currencies.")
            return None

        # Convert to USD and then to target currency
        amount_in_usd = amount / self.rates[from_currency]
        converted_amount = round(amount_in_usd * self.rates[to_currency], 2)
        return converted_amount

# Tkinter App UI
class CurrencyApp(ttk.Window):
    def __init__(self):
        super().__init__(themename="flatly")  # Try themes: flatly, superhero, darkly, cyborg, etc.

        self.title("💱 Modern Currency Converter")
        self.geometry("450x400")
        self.resizable(False, False)

        self.converter = CurrencyConverter()
        self.currencies = list(self.converter.rates.keys())

        self.create_widgets()

    def create_widgets(self):
        # Title
        ttk.Label(self, text="Currency Converter", font=("Helvetica", 20, "bold")).pack(pady=20)

        # Input form
        form = ttk.Frame(self, padding=20)
        form.pack()

        # Amount
        ttk.Label(form, text="Amount", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.amount_entry = ttk.Entry(form, font=("Helvetica", 12), width=22)
        self.amount_entry.grid(row=0, column=1)

        # From currency
        ttk.Label(form, text="From", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.from_currency = ttk.Combobox(form, values=self.currencies, state="readonly", width=20)
        self.from_currency.set("USD")
        self.from_currency.grid(row=1, column=1)

        # To currency
        ttk.Label(form, text="To", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.to_currency = ttk.Combobox(form, values=self.currencies, state="readonly", width=20)
        self.to_currency.set("INR")
        self.to_currency.grid(row=2, column=1)

        # Convert button
        convert_btn = ttk.Button(self, text="Convert 💱", bootstyle="success", command=self.convert_currency)
        convert_btn.pack(pady=20)

        # Result display
        self.result_label = ttk.Label(self, text="", font=("Helvetica", 14, "bold"), anchor="center")
        self.result_label.pack()

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_cur = self.from_currency.get()
            to_cur = self.to_currency.get()

            result = self.converter.convert(from_cur, to_cur, amount)
            if result is not None:
                self.result_label.config(text=f"{amount:.2f} {from_cur} = {result:.2f} {to_cur}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")

# Run app
if __name__ == "__main__":
    app = CurrencyApp()
    app.mainloop()
