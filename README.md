# Currency-Converter

A modern, user-friendly currency converter built with Python's `tkinter` and styled using `ttkbootstrap`. This application lets you convert between multiple popular currencies **without requiring any API** — using predefined exchange rates.

### 📸 Screenshot
![Screenshot 2025-06-02 111453](https://github.com/user-attachments/assets/293ca4f2-bddc-4963-b2dc-0dc49be9274e)



### 🖥️ Features

* Beautiful GUI using modern `ttkbootstrap` themes
* Dropdowns to select currencies (no typing needed)
* Converts between:

  * USD, EUR, INR, GBP, AUD, CAD, JPY, CHF
* Error handling for invalid inputs
* Lightweight and offline (no API key required)

---

### 📦 Requirements

* Python 3.x
* [`ttkbootstrap`](https://ttkbootstrap.readthedocs.io/)

Install via pip:

```bash
pip install ttkbootstrap
```

---

### 🚀 How to Run

1. Save the script as `currency_converter.py`.
2. Open terminal or command prompt.
3. Run the script:

```bash
python currency_converter.py
```

---

### 🧠 Exchange Rates Used (Hardcoded)

| Currency | Rate (vs USD) |
| -------- | ------------- |
| USD      | 1.00          |
| EUR      | 0.92          |
| INR      | 82.01         |
| GBP      | 0.77          |
| AUD      | 1.46          |
| CAD      | 1.36          |
| JPY      | 156.45        |
| CHF      | 0.91          |

*Note: Rates are static. You can update them inside the `CurrencyConverter` class.*

---


### ✨ Customization

* To change the theme:
  Replace `themename="flatly"` with other themes like `"superhero"`, `"darkly"`, `"cyborg"`, etc.
* To add more currencies:
  Add entries to the `rates` dictionary in the `CurrencyConverter` class.

---

### 📜 License

This project is free to use and modify for educational or personal purposes.


