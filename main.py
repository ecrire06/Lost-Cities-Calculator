import tkinter as tk

value = 0


class App(tk.Tk):

  def __init__(self):
    super().__init__()
    self.buttons = {}
    self.title("Lost City Calculator")

  def create_button(self, txt, setBg, x, y, cmd):
    button = tk.Button(self,
                       text=txt,
                       width=1,
                       height=1,
                       bg=setBg,
                       command=cmd)
    button.grid(row=y, column=x)
    self.buttons[(x + 1, y)] = button

  def change_hand(self, x, y=1):
    btn = self.buttons[(x, 1)]
    if btn.cget('text') == '-':
      btn.config(text='x')
    elif btn.cget('text') == 'x':
      btn.config(text='xx')
    elif btn.cget('text') == 'xx':
      btn.config(text='xxx')
    else:
      btn.config(text='-')


def press(num):
  global value
  value += int(num)
  equation.set(value)


def clear():
  global value
  value = 0
  equation.set(0)


if __name__ == "__main__":

  app = App()

  equation = tk.IntVar()
  expression_field = tk.Entry(app, textvariable=equation)
  expression_field.grid(columnspan=6, ipadx=70)

  for x in range(6):
    app.create_button('-', 'grey', x, 1, lambda k=x: app.change_hand(k + 1, 1))
    for y in range(9):
      app.create_button(f'{y+2}', 'white', x, y + 2, lambda k=y: press(k + 2))

  app.create_button('Clear', 'white', 5, 14, clear)

  print(app.buttons[(1, 1)].cget('text'))
  app.mainloop()
