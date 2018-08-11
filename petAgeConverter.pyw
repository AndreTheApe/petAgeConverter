# Code By AndreTheApe
import tkinter as tk
from functools import partial
import random
from random import randint

ageVal = "Human"

def Age_Year(set_age):
    global ageVal
    ageVal = set_age


# Conversation Code
def call_convert(rlabel1, rlabe12, inputn):
    tem = inputn.get()

    if ageVal == 'Human':
        d = float((float(tem) / 15) + random.uniform(0.0, 1.3))
        c = float((float(tem) / 15) + random.uniform(0.9, 1.5))
        rlabel1.config(text="Approximate Age In Dog Years Is %f" % d)
        rlabe12.config(text="Approximate Age In Cat Years Is %f" % c)
    if ageVal == 'Dog':
        h = float((float(tem) * 15) + random.uniform(0.0, 1.5))
        c = float((float(tem) * 1.0) + random.uniform(0.0, 0.3))
        rlabel1.config(text="Approximate Age In Human Years Is %f" % h)
        rlabe12.config(text="Approximate Age In Cat Years Is %f" % c)
    if ageVal == 'Cat':
        h = float((float(tem) * 7) + random.uniform(1.0, 1.3))
        d = float((float(tem) / 1.0) + random.uniform(0.0, 0.3))
        rlabel1.config(text="Approximate Age In Human Years Is %f" % h)
        rlabe12.config(text="Approximate Age In Dog Years Is %f" % d)
    return

# App Window
root = tk.Tk()
root.geometry()
root.title("Pet's Age Converter")
root.configure(background='#34495E')
root.resizable(width=True, height=True)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

numberInput = tk.StringVar()
var = tk.StringVar()

# Entry
input_label = tk.Label(root, text="Please Enter Age:", background='#5D6D7E', foreground="#FFFFFF")
input_entry = tk.Entry(root, textvariable=numberInput)
input_label.grid(row=1)
input_entry.grid(row=1, column=1)

# Display The Converted Years
result_label1 = tk.Label(root, background='#5D6D7E', foreground="#FFFFFF")
result_label1.grid(row=3, columnspan=4)
result_label2 = tk.Label(root, background='#5D6D7E', foreground="#FFFFFF")
result_label2.grid(row=4, columnspan=4)

# Menu Select
dropDownList = ["Human", "Dog", "Cat" ]
dropdown = tk.OptionMenu(root, var, *dropDownList, command=Age_Year)
var.set(dropDownList[0])
dropdown.grid(row=1, column=3)
dropdown.config(background='#5D6D7E', foreground="#FFFFFF")
dropdown["menu"].config(background='#5D6D7E  ', foreground="#FFFFFF")

# Button Click
call_convert = partial(call_convert, result_label1, result_label2, numberInput)
result_button = tk.Button(root, text="Convert", command=call_convert, background='#5D6D7E', foreground="#FFFFFF")
result_button.grid(row=2, columnspan=4)

root.mainloop()
