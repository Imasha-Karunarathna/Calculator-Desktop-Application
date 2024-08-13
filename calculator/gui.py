import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        elif operation == '**':
            result = num1 ** num2
        elif operation == '%':
            result = num1 % num2
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Function to clear input fields
def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("800x600")  # Set window size
root.configure(bg="#000000")  # Set background color

# Input fields for numbers with custom font
entry1 = tk.Entry(root, width=15, font=("Arial", 12))
entry1.grid(row=0, column=1, padx=20, pady=20)
entry2 = tk.Entry(root, width=15, font=("Arial", 12))
entry2.grid(row=1, column=1, padx=20, pady=20)

# Labels for input fields with custom font and color
tk.Label(root, text="First Number:", font=("Arial", 12), fg="black", bg="#ffff00").grid(row=0, column=0, padx=20, pady=20)
tk.Label(root, text="Second Number:", font=("Arial", 12), fg="black", bg="#ffff00").grid(row=1, column=0, padx=20, pady=20)

# Dropdown menu for operation selection
operation_var = tk.StringVar(root)
operation_var.set('+')  # Default value

operation_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/', '**', '%')
operation_menu.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Operation:", font=("Arial", 12), fg="black", bg="#ffff00").grid(row=2, column=0)

# Button to perform the calculation with custom font and color
calculate_button = tk.Button(root, text="Calculate", font=("Arial", 12), fg="white", bg="green", command=calculate)
calculate_button.grid(row=3, column=1, padx=20, pady=20, sticky="ew")

# Clear button
clear_button = tk.Button(root, text="Clear", font=("Arial", 12), fg="white", bg="red", command=clear_fields)
clear_button.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

# Label to display the result with custom font and color
result_label = tk.Label(root, text="Result: ", font=("Arial", 34))
result_label.grid(row=4, column=1, padx=20, pady=20)

# Run the main loop
root.mainloop()
