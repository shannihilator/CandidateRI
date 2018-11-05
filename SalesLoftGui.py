# -*- coding: utf-8 -*-
"""
Created on ‎Saturday, ‎November ‎3, ‎2018, ‏‎2:25:35 PM

@author: Rahul Isaac
"""
from tkinter import N, S, W, E, Frame, Button
from tkinter.ttk import Treeview, Scrollbar


class SalesLoftGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        master.title("SalesLoft People Data")
        self.pack()
        
        self.frameButtons = Frame(self)
        self.frameButtons.pack()
        
    def addTable(self, data, columns, columnNames):
        #Set up the table
        frame = Frame(self)
        frame.pack()        
        
        tv = Treeview(frame)
        tv.pack(side="left")  
        
        vsb = Scrollbar(frame, orient="vertical", command=tv.yview)
        vsb.pack(side='right', fill='y')
    
        tv.configure(yscrollcommand=vsb.set)
        
        #Set up the first column
        tv.heading("#0", text=columnNames[0])
        tv['columns'] = tuple(columns[1:])
        
        #Set up the remaining columns
        for col, colName in zip(columns[1:], columnNames[1:]):
            tv.heading(col, text=colName)
        
        #Add the data
        for d in data:
            row = []
            for c in columns[1:]: 
                row.append(d[c])
            tv.insert('', 'end', text=d[columns[0]], values = tuple(row))
        

    def addButton(self, buttonText, onClick):
        b = Button(self.frameButtons, text=buttonText, command=onClick)
        b.pack(side="left")
