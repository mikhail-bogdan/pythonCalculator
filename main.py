from tkinter import *


first_value = 10
operation = -1
global textData


def create_button(root, buttonText, callback):
    button = Button(root, text=buttonText, width=3, font=("Verdana", 22), command=callback)
    button.pack(side=LEFT, expand=True, fill=BOTH)
    return button


def plus_clicked():
    global first_value
    global operation
    try:
        first_value = int(textData.get())
        operation = 0
        textData.set("0")
    except ValueError:
        return


def minus_clicked():
    global first_value
    global operation
    try:
        first_value = int(textData.get())
        operation = 1
        textData.set("0")
    except ValueError:
        return


def multiply_clicked():
    global first_value
    global operation
    try:
        first_value = int(textData.get())
        operation = 2
        textData.set("0")
    except ValueError:
        return


def divide_clicked():
    global first_value
    global operation
    try:
        first_value = int(textData.get())
        operation = 3
        textData.set("0")
    except ValueError:
        return


def clear_clicked():
    global first_value
    global operation
    first_value = None
    operation = -1
    textData.set("0")


def equal_clicked():
    global first_value
    global operation
    if operation == -1:
        return

    second_value = int(textData.get())
    result = 0

    if operation == 0:
        result = first_value + second_value
    elif operation == 1:
        result = first_value - second_value
    elif operation == 2:
        result = first_value * second_value
    elif operation == 3:
        if second_value != 0:
            result = first_value / second_value
        else:
            first_value = None
            operation = -1
            result = "Error"

    textData.set(str(result))


if __name__ == '__main__':
    root = Tk()
    root.geometry("200x200")
    root.title("Calculator")
    textData = StringVar()
    text = Entry(root, font=("Verdana", 22), justify=RIGHT, textvariable=textData)
    text.pack(expand=True, fill=BOTH)
    textData.set("0")
    frame1 = Frame(root)
    frame1.pack(expand=True, fill=BOTH)
    frame2 = Frame(root)
    frame2.pack(expand=True, fill=BOTH)

    create_button(frame1, "+", plus_clicked)
    create_button(frame1, "-", minus_clicked)
    create_button(frame1, "C", clear_clicked)
    create_button(frame2, "*", multiply_clicked)
    create_button(frame2, "/", divide_clicked)
    create_button(frame2, "=", equal_clicked)

    root.mainloop()
