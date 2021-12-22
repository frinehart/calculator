"""
Author: Francis Rinehart
Purpose: Calculator App
Language: Python
Last Update: 12/22/2021 at 18:29
"""

import tkinter as tk

# Colors to the calculator appearance
outside_color = "#000000"
black_color = "#000000"
blue_color = "#3365ff"
gray_color = "#3b3b3b"
digit_colors = "#FFFFFF"

# Font Styles to the calculator appearance
font_digits = ("Calibri", 19, "bold")
font_default = {"Calibri", 20}
font_small = ("Calibri", 16)
font_large = ("Calibri", 40, "bold")

# Creates Calculator Window
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("325x475") # Adjust the size of the calculator
        self.window.resizable(0, 0)
        self.window.title("Calculator") # Names the title of the calculator

        self.totalExpression = ''
        self.currentExpression = ''

        # Creates calculator frames
        self.displayFrame = self.createDisplayFrame()

        self.totalLabel, self.label = self.createDisplayLabels()

        # Dictionary list of Calculator digits
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1),
        }
        # Display different features on the calculator
        self.operations = {"/": "\u00F7", '*': "\u00D7", '-': '-', '+': '+'}
        self.buttonsFrame = self.createButtonsFrame()

        self.buttonsFrame.rowconfigure(0, weight=1)

        for x in range(1, 5):
            self.buttonsFrame.rowconfigure(x, weight=1)
            self.buttonsFrame.columnconfigure(x, weight=1)

        self.createDigitButtons()
        self.createOperatorButtons()
        self.createSpecialButtons()
        self.bindKeys()

    def bindKeys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit = key:
            self.addToExpression((digit)))

        for key in self.operations:
            self.window.bind(key, lambda event, operator = key:
            self.appendOperator(operator))

    # Creates different special buttons in the calculator
    def createSpecialButtons(self):
        self.createClearButton()
        self.createEqualsButton()
        self.createSquareButton()
        self.createSqrtButton()

    # Displays different labels on the calculator
    def createDisplayLabels(self):
        totalLabel = tk.Label(self.displayFrame,
                               text = self.totalExpression, anchor = tk.E,
                               bg = gray_color, fg = digit_colors, padx = 24,
                               font = font_small)
        totalLabel.pack(expand=True, fill = "both")

        label = tk.Label(self.displayFrame,
                               text=self.currentExpression, anchor=tk.E,
                               bg=gray_color, fg=digit_colors, padx=24,
                               font = font_large)
        label.pack(expand=True, fill="both")

        return totalLabel, label

    def createDisplayFrame(self):
        frame = tk.Frame(self.window, height = 221, bg = gray_color)
        frame.pack(expand = True, fill = "both")
        return frame

    def addToExpression(self, value):
        self.currentExpression += str(value)
        self.updateLabel()

    def createDigitButtons(self):
        for digit, gridValue in self.digits.items():
            button = tk.Button(self.buttonsFrame, text = str(digit), bg = black_color,
                               fg = digit_colors, font = font_digits,
                               borderwidth = 0, command=lambda x=digit:
                self.addToExpression(x))

            button.grid(row=gridValue[0], column=gridValue[1], sticky=tk.NSEW)

    def appendOperator(self, operator):
        self.currentExpression += operator
        self.totalExpression += self.currentExpression
        self.currentExpression = ''
        self.updateTotalLabel()
        self.updateLabel()


    def createOperatorButtons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttonsFrame, text = symbol,
                               bg=outside_color, fg=digit_colors, font=font_default,
                               borderwidth = 0, command = lambda x=operator: self.appendOperator(x))
            button.grid(row = i, column = 4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.currentExpression = ''
        self.totalExpression = ''
        self.updateLabel()
        self.updateTotalLabel()

    def createClearButton(self):
        button = tk.Button(self.buttonsFrame, text='C',
                           bg=outside_color, fg=digit_colors, font=font_default,
                           borderwidth=0, command= self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.currentExpression = str(eval(f"{self.currentExpression}**2"))
        self.updateLabel()

    def createSquareButton(self):
        button = tk.Button(self.buttonsFrame, text='x\u00b2',
                           bg=outside_color, fg=digit_colors, font=font_default,
                           borderwidth=0, command= self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.currentExpression = str(eval(f"{self.currentExpression}**0.5"))
        self.updateLabel()

    def createSqrtButton(self):
        button = tk.Button(self.buttonsFrame, text='\u221ax',
                           bg=outside_color, fg=digit_colors, font=font_default,
                           borderwidth=0, command= self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.totalExpression += self.currentExpression
        self.updateTotalLabel()
        try:
            self.currentExpression = str(eval(self.totalExpression))
            self.totalExpression = ''
        except Exception as e:
            self.currentExpression = "Error"
        finally:
            self.updateLabel()

        self.updateLabel()

    def createEqualsButton(self):
        button = tk.Button(self.buttonsFrame, text='=',
                           bg=blue_color, fg=digit_colors, font=font_default,
                           borderwidth=0, command = self.evaluate)
        button.grid(row=4, column=3, columnspan = 2, sticky=tk.NSEW)

    def createButtonsFrame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand = True, fill = "both")
        return frame

    def updateTotalLabel(self):
        expression = self.totalExpression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.totalLabel.config(text = expression)

    def updateLabel(self):
        self.label.config(text = self.currentExpression[:11])

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    cal = Calculator()
    cal.run()
