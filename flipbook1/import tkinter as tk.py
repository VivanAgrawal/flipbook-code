import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # Variable to store the current expression
        self.expression = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        # Create the UI
        self.create_ui()

    def create_ui(self):
        # Result display
        result_frame = ttk.Frame(self.root)
        result_frame.pack(fill=tk.BOTH, padx=10, pady=10)

        result_label = ttk.Label(result_frame, textvariable=self.result_var,
                                font=("Arial", 20), anchor="e")
        result_label.pack(fill=tk.BOTH)

        # Button frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Configure grid
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)

        # Create buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 0, 0), ('CE', 0, 1), ('(', 0, 2), (')', 0, 3)
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(button_frame, text=text, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

    def button_click(self, value):
        if value == '=':
            # Calculate the result
            try:
                result = eval(self.expression)
                self.result_var.set(result)
                self.expression = str(result)
            except:
                self.result_var.set("Error")
                self.expression = ""
        elif value == 'C':
            # Clear all
            self.expression = ""
            self.result_var.set("0")
        elif value == 'CE':
            # Clear entry (last character)
            self.expression = self.expression[:-1]
            if not self.expression:
                self.result_var.set("0")
            else:
                self.result_var.set(self.expression)
        else:
            # Add to expression
            self.expression += value
            self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()