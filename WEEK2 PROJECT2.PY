import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(*args):
    try:
        celsius = float(celsius_var.get())
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_var.set(f"{fahrenheit:.2f}")
    except ValueError:
        fahrenheit_var.set("")

def fahrenheit_to_celsius(*args):
    try:
        fahrenheit = float(fahrenheit_var.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius_var.set(f"{celsius:.2f}")
    except ValueError:
        celsius_var.set("")

def validate_input(new_value):
    if new_value == "" or new_value.replace(".", "", 1).isdigit():
        return True
    return False

root = tk.Tk()
root.title("Temperature Converter")

celsius_var = tk.StringVar()
fahrenheit_var = tk.StringVar()

validate_command = (root.register(validate_input), "%P")

celsius_label = ttk.Label(root, text="Celsius:")
celsius_label.grid(column=0, row=0, padx=10, pady=10)

celsius_entry = ttk.Entry(root, textvariable=celsius_var, validate="key", validatecommand=validate_command)
celsius_entry.grid(column=1, row=0, padx=10, pady=10)
celsius_var.trace_add("write", celsius_to_fahrenheit)

fahrenheit_label = ttk.Label(root, text="Fahrenheit:")
fahrenheit_label.grid(column=0, row=1, padx=10, pady=10)

fahrenheit_entry = ttk.Entry(root, textvariable=fahrenheit_var, validate="key", validatecommand=validate_command)
fahrenheit_entry.grid(column=1, row=1, padx=10, pady=10)
fahrenheit_var.trace_add("write", fahrenheit_to_celsius)

root.mainloop()