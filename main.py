from tkinter import *
import tkinter as tk

class MyApp:

  def __init__(self, root):
    root.title("My app")
    root.geometry("500x400")
    root.maxsize(600,400)

    frame = Frame(root, width=200, height=100, borderwidth = 2, relief="groove")
    #frame.place(x=0, y=0)

    self.label_text = StringVar()
    label = Label(root, text="Some label text", textvariable=self.label_text)
    #label.pack(side=tk.LEFT)
    label.grid(column=1, row=1)
    label.configure(text = "New label text", font = ("Courier", 40))

    self.entry_text = StringVar()
    entry = Entry(root, textvariable=self.entry_text)
    entry.grid(column=3, row=1)
    #entry.pack(side=tk.LEFT)

    button = Button(root, text="Press me", command=self.press_button)
    #button.place(x=0, y=0)
    #button.configure(font = ("Courier", 40), width=10, height=2)
    button.grid(column=1, row=2, sticky=(S, E, W))
    #button.pack(side=tk.LEFT)

    self.list_item_strings = ["Hey", "Hi", "Hello", "Howdy", "Greetings"]
    list_items = StringVar(value=self.list_item_strings)
    listbox = Listbox(root, listvariable=list_items)
    #listbox.pack(side=tk.LEFT, padx=40, pady=20)
    listbox["height"] = 3
    listbox.bind("<<ListboxSelect>>", lambda s: self.select_item(listbox.curselection()))
    listbox.grid(column=2, row=2)

  def press_button(self):
    text = self.entry_text.get()
    self.label_text.set(text)
    print("Button pressed")

  def select_item(self, index):
    selected_item = self.list_item_strings[index[0]]
    print(selected_item)



root = Tk()
MyApp(root)
root.mainloop()
