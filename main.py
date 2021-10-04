from tkinter import *

class MyApp:

  def __init__(self, root):
    root.title("My app")
    root.geometry("500x400")
    root.maxsize(600,400)


    self.label_text = StringVar()
    label = Label(root, text="Some label text", textvariable=self.label_text)
    label.pack()

    #label["text"] = "New label text"
    #label["font"] = ("Courier", 40)
    label.configure(text = "New label text", font = ("Courier", 40))

    self.entry_text = StringVar()
    entry = Entry(root, textvariable=self.entry_text)
    entry.pack()

    button = Button(root, text="Press me", command=self.press_button)
    button.pack()

  def press_button(self):
    text = self.entry_text.get()
    self.label_text.set(text)
    print("Button pressed")



root = Tk()
MyApp(root)
root.mainloop()
