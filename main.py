from tkinter import *

class MyApp:

  def __init__(self, root):
    root.title("My app")
    root.geometry("500x400")
    root.maxsize(600,400)

    label = Label(root, text="Some label text")
    label.pack()

    label["text"] = "New label text"

root = Tk()
MyApp(root)
root.mainloop()
