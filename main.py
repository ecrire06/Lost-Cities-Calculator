from tkinter import *
import tkinter as tk

value = 0

def press(num):
  global value
  value += int(num)
  equation.set(value)


def clear():
  global value
  value = 0
  equation.set(0)


#def save():
#  global expression


if __name__ == "__main__":
  gui = Tk()
  gui.title("Lost City Calculator")
  equation = IntVar()
  expression_field = Entry(gui, textvariable=equation)
  expression_field.grid(columnspan=6, ipadx=70)
  for i in range(10):
    for j in range(6):
      text = i + 1 if i != 0 else 'x'
      btn = Button(gui,
                   text=f'{text}',
                   fg='black',
                   bg='white',
                   activebackground='grey',
                   command=lambda k=i: press(k + 1),
                   height=1,
                   width=1)
      btn.grid(row=i + 1, column=j)
#  save = Button(gui,
#                test='Save',
#                fg='black',
#                bg='white',
#                activebackground='grey',
#                commane=save,
#                height=1,
#                width=1)
#  save.grid(row=12, column=4)
  clear = Button(gui,
                 text='Clear',
                 fg='black',
                 bg='white',
                 activebackground='grey',
                 command=clear,
                 height=1,
                 width=1)
  clear.grid(row=12, column=5)
  gui.mainloop()
