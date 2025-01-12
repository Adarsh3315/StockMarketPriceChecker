import tkinter as tk
from tkinter import messagebox
import yfinance as yf


def fetch_and_display_stock_price(stock_symbol):
    try:
        stock = yf.Ticker(stock_symbol)
        quote = stock.history(period="1d")
        if not quote.empty:
            price = quote["Close"].iloc[-1]

            if ".BO" in stock_symbol or ".NS" in stock_symbol:
                current_stock.set(f"₹{price:.2f} (INR)")
            else:
                current_stock.set(f"${price:.2f} (USD)")

            status_label.config(text="Price Fetched Successfully!!", fg="#009500")
        else:
            raise ValueError("Invalid Stock Symbol Or Data Not Available.")
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
        status_label.config(
            text="Invalid Stock Symbol Or Data Not Available.", fg="#ffea00"
        )
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        status_label.config(text="An error occurred.", fg="red")


def stock_price():
    stock_symbol = stock_entry_var.get().upper().strip()
    stock_entry.delete(0, tk.END)
    stock_entry.insert(0, stock_symbol)

    if not stock_symbol:
        messagebox.showwarning("Warning", "Stock Symbol Cannot Be Empty.")
        status_label.config(text="Please Enter Valid Stock Symbol.", fg="#ffea00")
        return

    fetch_and_display_stock_price(stock_symbol)


def force_uppercase(*args):
    stock_entry_var.set(stock_entry_var.get().upper())


def show_about():
    messagebox.showinfo(
        "About", "Stock Market Price Checker\nVersion 1.0\nDeveloped By A&J"
    )


def show_help():
    messagebox.showinfo(
        "Help",
        "Enter Stock Symbol (Example, AMZN or TATASTEEL.BO or TCS.NS) And Click 'Show Price' To Get Current Stock Price.",
    )


root = tk.Tk()
root.title("Stock Market Price Checker Developed By A&J")
root.geometry("1920x1080")
root.configure(bg="#343f71")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)
help_menu.add_command(label="Help", command=show_help)

title_label = tk.Label(
    root,
    text="Stock Market Price Checker",
    font=("Arial", 30, "bold"),
    bg="#343f71",
    fg="#ffffff",
)
title_label.pack(pady=20)

stock_entry_var = tk.StringVar()
stock_entry_var.trace_add("write", force_uppercase)
stock_entry = tk.Entry(
    root, textvariable=stock_entry_var, font=("Arial", 15), width=20, justify="center"
)
stock_entry.pack(pady=10)

fetch_button = tk.Button(
    root,
    text="Show Price",
    command=stock_price,
    font=("Arial", 15),
    bg="#e74c3c",
    fg="#ffffff",
    activebackground="#3498db",
    activeforeground="#000000",
)
fetch_button.pack(pady=10)

result_label = tk.Label(
    root, text="Stock Result:", font=("Arial", 15), bg="#343f71", fg="#ffffff"
)
result_label.pack(pady=10)

current_stock = tk.StringVar()
result2 = tk.Label(
    root,
    text="",
    textvariable=current_stock,
    font=("Arial", 15),
    bg="#343f71",
    fg="#ffffff",
)
result2.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 15), bg="#343f71", fg="#ffffff")
status_label.pack(pady=10)

footer_label = tk.Label(
    root, text="Developed By A&J", font=("Arial", 15), bg="#343f71", fg="#ffea00"
)
footer_label.pack(side="bottom", pady=10)

root.mainloop()
