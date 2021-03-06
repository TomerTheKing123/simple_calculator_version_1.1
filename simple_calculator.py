import tkinter
import math

math_action = ""  # This variable contains the math action
root = tkinter.Tk()

root.title("Simple Calculator")

entry = tkinter.Entry(root, width = 45, borderwidth = 1)
entry.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def button_click(number):
    current = entry.get()
    entry.delete(0, tkinter.END)
    entry.insert(0, str(current) + str(number))  # Inserts the number to the Entry

def button_clear_action():
    entry.delete(0, tkinter.END)  # Removes everything in entry

def button_decimal():
    entry.insert(tkinter.END, ".")  #Adds decimal dot on screen

def button_left_parenthes_action():
    pass
    #TODO-Complete

def button_right_parenthes_action():
    pass
    #TODO-Complete

def button_add_action():
    """addtion action"""
    number = entry.get()
    global first_number
    first_number = float(number)  # Save the first number typed for the math action
    entry.delete(0, tkinter.END)

    global math_action
    math_action = "+"

def button_subtract_action():
    """subtract action"""
    number = entry.get()
    global first_number
    first_number = float(number)  # Saves the first number typed for the math action
    entry.delete(0, tkinter.END)

    global math_action
    math_action = "-"

def button_multiply_action():
    """multiply action"""
    number = entry.get()
    global first_number
    first_number = float(number)  # Saves the first number typed for the math action
    entry.delete(0, tkinter.END)

    global math_action
    math_action = "*"

def button_divide_action():
    """divide action"""
    number = entry.get()
    global first_number
    first_number = float(number)  # Saves the first number typed for the math action
    entry.delete(0, tkinter.END)

    global math_action
    math_action = "/"

def button_factorial_action():
    """factorial action"""
    number = entry.get()
    global first_number
    first_number = float(number)  # Saves the first number typed for the math action
    entry.delete(0, tkinter.END)

    global math_action
    math_action = "!"





def button_equal():
    

    if math_action == "!":
        entry.insert(0, math.factorial(first_number))

    else:

        second_number = float(entry.get())  # Saves the second number
        entry.delete(0, tkinter.END)

        if math_action == "+":
            if first_number.is_integer() and second_number.is_integer():  # Checks if both numbers are integers. If so, it will return an integer
                entry.insert(0, int(first_number + second_number))  # Shows the result on screen

            elif (first_number + second_number).is_integer():  # Checks if the result is an integer. If so, it will return an integer
                entry.insert(0, int(first_number + second_number))  # Shows the result on screen

            else:
                entry.insert(0, first_number + second_number)  # shows the result on screen

        if math_action == "-":

            if first_number.is_integer() and second_number.is_integer():  # Checks if both numbers are integers. If so, it will return an integer
                entry.insert(0, int(first_number - second_number))  # Shows the result on screen

            elif (first_number - second_number).is_integer():  # Checks if the result is an integer. If so, it will return an integer
                entry.insert(0, int(first_number - second_number))  # Shows the result on screen

            else:
                entry.insert(0, first_number - second_number)  # Shows the result on screen

        if math_action == "*":

            if first_number.is_integer() and second_number.is_integer():  # Checks if both numbers are integers. If so, it will return an integer
                entry.insert(0, int(first_number * second_number))  # Shows the result on screen

            elif (first_number * second_number).is_integer():  # Checks if the result is an integer. If so, it will return an integer
                entry.insert(0, int(first_number * second_number))  # Shows the result on screen

            else:
                entry.insert(0, first_number * second_number)  # Shows the result on screen

        if math_action == "/":
            if first_number.is_integer() and second_number.is_integer() and (first_number / second_number).is_integer():  # Checks if the numbers are integers and if their result is an integer. If so, then it will return an integer
                entry.insert(0, int(first_number / second_number))  # Shows the result on screen

            elif (first_number / second_number).is_integer():  # If the result of this 2 numbers is integer then it will return an integer
                entry.insert(0, int(first_number / second_number))  # Shows the result on screen

            else:  # If it reached here it means
                entry.insert(0, first_number / second_number)  # Shows the result on screen






def main():


    # Create the buttons
    button0 = tkinter.Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0), bg = "snow")
    button1 = tkinter.Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1), bg = "snow")
    button2 = tkinter.Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2), bg = "snow")
    button3 = tkinter.Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3), bg = "snow")
    button4 = tkinter.Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4), bg = "snow")
    button5 = tkinter.Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5), bg = "snow")
    button6 = tkinter.Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6), bg = "snow")
    button7 = tkinter.Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7), bg = "snow")
    button8 = tkinter.Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8), bg = "snow")
    button9 = tkinter.Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9), bg = "snow")

    button_add = tkinter.Button(root, text = "+", padx = 40, pady = 20, command = button_add_action)
    button_subtract = tkinter.Button(root, text = "-", padx = 40, pady = 20, command = button_subtract_action)
    button_multiply = tkinter.Button(root, text = "*", padx = 40, pady = 20, command = button_multiply_action)
    button_divide = tkinter.Button(root, text = "/", padx = 40, pady = 20, command = button_divide_action)
    button_factorial = tkinter.Button(root, text = "!", padx = 40, pady = 20, command = button_factorial_action)

    button_equals = tkinter.Button(root, text = "=", padx = 40, pady = 20, command = button_equal, bg = "deep sky blue")

    button_clear = tkinter.Button(root, text = "C", padx = 40, pady = 20, command = button_clear_action)

    button_decimal_dot = tkinter.Button(root, text = ".", padx = 40, pady = 20, command = button_decimal)

    button_left_parenthes = tkinter.Button(root, text = "(", padx = 40, pady = 20, command = button_left_parenthes_action)
    button_right_parenthes = tkinter.Button(root, text = ")", padx = 40, pady = 20, command = button_right_parenthes_action)

    # Create the buttons
    # TODO-Add more math actions buttons

    #Puts the buttons on screen
    button7.grid(row = 2, column = 0)
    button8.grid(row = 2, column = 1)
    button9.grid(row = 2, column = 2)

    button4.grid(row = 3, column = 0)
    button5.grid(row = 3, column = 1)
    button6.grid(row = 3, column = 2)

    button1.grid(row = 4, column = 0)
    button2.grid(row = 4, column = 1)
    button3.grid(row = 4, column = 2)

    button0.grid(row = 5, column = 1)

    button_add.grid(row = 2, column = 3)
    button_subtract.grid(row = 3, column = 3)
    button_multiply.grid(row = 4, column = 3)
    button_divide.grid(row = 5, column = 3)
    button_factorial.grid(row = 6, column = 2)

    button_equals.grid(row = 5, column = 2)

    button_clear.grid(row = 5, column = 0)

    button_decimal_dot.grid(row = 6, column = 3)

    button_left_parenthes.grid(row = 6, column = 0)
    button_right_parenthes.grid(row = 6, column = 1)
    # Puts the buttons on screen


    root.mainloop()


if __name__ == "__main__":
    main()
