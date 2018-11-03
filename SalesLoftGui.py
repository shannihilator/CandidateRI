from tkinter import Tk

class SalesLoftGUI:
    def __init__(self, master):
        self.master = master
        master.title("SalesLoft People Data")

root = Tk()
my_gui = SalesLoftGUI(root)
root.mainloop()
