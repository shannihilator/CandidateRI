from tkinter import N, S, W, E, Frame
from tkinter.ttk import Treeview


class SalesLoftGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        master.title("SalesLoft People Data")
        self.grid()
                             
    def addTable(self, data, columns, columnNames):
        #Set up the table
        tv = Treeview(self)
        
        #Set up the first column
        tv.heading("#0", text=columnNames[0])
        tv['columns'] = tuple(columns[1:])
        
        #Set up the remaining columns
        for col, colName in zip(columns[1:], columnNames[1:]):
            tv.heading(col, text=colName)
        
        tv.grid(sticky = (N,W))
        
        #Add the data
        for d in data:
            row = []
            for c in columns[1:]: 
                row.append(d[c])
            tv.insert('', 'end', text=d[columns[0]], values = tuple(row))
