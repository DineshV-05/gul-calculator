import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("360x520")
window.resizable(False, False)

# Entry widget to display numbers and results
entry = tk.Entry(window, width=16, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Global expression string
expression = ""

# Function to update the expression
def press(num):
    global expression
    expression += str(num)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

# Function to evaluate the result
def equal():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = result  # so next input continues from result
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

# Function to clear the entry
def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Add buttons to window
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=equal)
    else:
        btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: press(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(window, text='C', width=22, height=2, font=("Arial", 18), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

# Run the GUI event loop
window.mainloop()
