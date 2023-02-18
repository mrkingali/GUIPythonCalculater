import tkinter as tk

if __name__ == '__main__':
    cal = ""


    def addToCal(input1):
        global cal
        cal = cal + str(input1)
        textField.delete(1.0, "end")
        textField.insert(1.0, cal)


    def clearCal():
        global cal
        cal = ""
        textField.delete(1.0, "end")


    def evaluateCal():
        global cal
        try:
            cal = str(eval(cal))
            textField.delete(1.0, "end")
            textField.insert(1.0, cal)
        except:

            clearCal()
            textField.insert(1.0, "error")


    root = tk.Tk()
    root.geometry("300x275")

    textField = tk.Text(root, height=2, width=16, font=("Arial", 24))
    textField.grid(row=0, column=0, columnspan=5)

    btn_one = tk.Button(root, text="1", command=lambda: addToCal("1"), width=5, font=("Arial", 14))
    btn_one.grid(row=1, column=0)
    btn_two = tk.Button(root, text="2", command=lambda: addToCal("2"), width=5, font=("Arial", 14))
    btn_two.grid(row=1, column=1)
    btn_tree = tk.Button(root, text="3", command=lambda: addToCal("3"), width=5, font=("Arial", 14))
    btn_tree.grid(row=1, column=2)
    btn_four = tk.Button(root, text="4", command=lambda: addToCal("4"), width=5, font=("Arial", 14))
    btn_four.grid(row=2, column=0)
    btn_five = tk.Button(root, text="5", command=lambda: addToCal("5"), width=5, font=("Arial", 14))
    btn_five.grid(row=2, column=1)
    btn_six = tk.Button(root, text="6", command=lambda: addToCal("6"), width=5, font=("Arial", 14))
    btn_six.grid(row=2, column=2)
    btn_seven = tk.Button(root, text="7", command=lambda: addToCal("7"), width=5, font=("Arial", 14))
    btn_seven.grid(row=3, column=0)
    btn_eight = tk.Button(root, text="8", command=lambda: addToCal("8"), width=5, font=("Arial", 14))
    btn_eight.grid(row=3, column=1)
    btn_nine = tk.Button(root, text="9", command=lambda: addToCal("9"), width=5, font=("Arial", 14))
    btn_nine.grid(row=3, column=2)
    btn_zero = tk.Button(root, text="0", command=lambda: addToCal("0"), width=5, font=("Arial", 14))
    btn_zero.grid(row=4, column=1)

    btn_open = tk.Button(root, text="(", command=lambda: addToCal("("), width=5, font=("Arial", 14))
    btn_open.grid(row=4, column=0)
    btn_close = tk.Button(root, text=")", command=lambda: addToCal(")"), width=5, font=("Arial", 14))
    btn_close.grid(row=4, column=2)

    btn_equal = tk.Button(root, text="=", command=lambda: evaluateCal(), width=11, font=("Arial", 14))
    btn_equal.grid(row=5, column=2, columnspan=2)

    btn_clear = tk.Button(root, text="C", command=lambda: clearCal(), width=11, font=("Arial", 14))
    btn_clear.grid(row=5, column=0, columnspan=2)

    btn_sum = tk.Button(root, text="+", command=lambda: addToCal("+"), width=5, font=("Arial", 14))
    btn_sum.grid(row=4, column=3)
    btn_multi = tk.Button(root, text="*", command=lambda: addToCal("*"), width=5, font=("Arial", 14))
    btn_multi.grid(row=1, column=3)
    btn_div = tk.Button(root, text="/", command=lambda: addToCal("/"), width=5, font=("Arial", 14))
    btn_div.grid(row=2, column=3)
    btn_min = tk.Button(root, text="-", command=lambda: addToCal("-"), width=5, font=("Arial", 14))
    btn_min.grid(row=3, column=3)

    root.mainloop()
