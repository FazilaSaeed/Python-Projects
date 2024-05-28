import tkinter as tk

# Function to perform arithmetic operations
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Error! Division by zero"
            else:
                result = num1 / num2

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Invalid input")

# Create a Tkinter window
window = tk.Tk()
window.title("Simple Calculator")

# Create input fields
entry1 = tk.Entry(window)
entry1.grid(row=0, column=0)

operator = tk.StringVar(window)
operator.set("+")  # Default operation is addition

entry2 = tk.Entry(window)
entry2.grid(row=0, column=2)

# Create operation dropdown
operation_menu = tk.OptionMenu(window, operator, "+", "-", "*", "/")
operation_menu.grid(row=0, column=1)

# Create calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=1)

# Create label to display result
result_label = tk.Label(window, text="")
result_label.grid(row=2, column=0, columnspan=3)

# Run the Tkinter event loop
window.mainloop()
