import sys
import os
import tkinter as tk

value = 0


# =======CUSTOM FUNCTIONS=======
def hand(event):
  btn = event.widget
  if btn.cget('text') == '-':
    btn.config(text='x')
  elif btn.cget('text') == 'x':
    btn.config(text='xx')
  elif btn.cget('text') == 'xx':
    btn.config(text='xxx')
  else:
    btn.config(text='-')


def num(event):
  btn = event.widget
  global value

  if btn.cget('bg') == 'grey':
    value -= int(btn.cget('text'))
    btn.config(bg='yellow')
  else:
    value += int(btn.cget('text'))
    btn.config(bg="grey")

  equation.set(value)


def restart_program(event):
  """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
  python = sys.executable
  os.execl(python, python, *sys.argv)


# =======APP CLASS=======
class App(tk.Tk):

  def __init__(self):
    super().__init__()
    self.buttons = {}
    self.title("Lost City Calculator")

  def create_button(self, txt, setBg, x, y, type):
    button = tk.Button(self, text=txt, width=1, height=1, bg=setBg)
    if type == 'hand':
      button.bind('<1>', hand)
    elif type == 'num':
      button.bind('<1>', num)
    elif type == 'clear':
      button.bind('<1>', restart_program)
    button.grid(row=y, column=x)
    self.buttons[(x + 1, y)] = button


# =======TKINTER=======
if __name__ == "__main__":

  app = App()

  equation = tk.IntVar()
  expression_field = tk.Entry(app, textvariable=equation)
  expression_field.grid(columnspan=6, ipadx=70)

  color = ['yellow', 'white', 'blue', 'green', 'red', 'purple']

  for x in range(6):
    app.create_button('-', 'grey', x, 1, 'hand')
    for y in range(9):
      app.create_button(f'{y+2}', color[x], x, y + 2, 'num')

  for i in range(6):
    col = tk.Label(app, text='0')
    col.grid(column=i, row=13)

  app.create_button('Clear', 'white', 5, 14, 'clear')

  app.mainloop()
