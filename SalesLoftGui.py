from tkinter import Tk, Label, Button

class SalesLoftGUI:
    def __init__(self, master):
        self.master = master
        master.title("SalesLoft People Data")

        self.labelTitle = Label(master, text="SalesLoft People Data")
        self.labelTitle.pack()


root = Tk()
my_gui = SalesLoftGUI(root)
root.mainloop()
