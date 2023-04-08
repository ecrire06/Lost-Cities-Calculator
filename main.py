import tkinter as tk

value = 0


class Checkers:

  def __init__(self, master):
    self.buttons = {}
    self.master = master
    master.title("Lost City Calculator")

  def create_button(self, txt, setBg, x, y, cmd):
    button = tk.Button(self.master, text=txt, width=1, height=1, bg=setBg, command=cmd)
    button.grid(row=y, column=x)
    self.buttons[(x+1, y)] = button

  def update_button(self, x, y, txt):
    self.buttons[(x+1, y)].configure(text=txt)


def press(num):
  global value
  value += int(num)
  equation.set(value)


def change_hand():
  pass


def clear():
  global value
  value = 0
  equation.set(0)


if __name__ == "__main__":

  root = tk.Tk()
  app = Checkers(root)

  equation = tk.IntVar()
  expression_field = tk.Entry(root, textvariable=equation)
  expression_field.grid(columnspan=6, ipadx=70)

  for x in range(6):
    app.create_button('-', 'grey', x, 1, change_hand())
    for y in range(9):
      app.create_button(f'{y+2}', 'white', x, y + 2, lambda k=y: press(k + 2))

  app.create_button('Clear', 'white', 5, 13, clear)
  
  root.mainloop()
  