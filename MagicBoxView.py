#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import tkinter as tk
# from tkinter import ttk
import webbrowser 

class MagicBoxView(tk.Frame):
    """Encapsulates of all the GUI logic.

   

    Attributes:
        master: where to open the Frame, by deafult root window
        title: Main Label
     
        one: Button 
        two: Button 
        three: Button 

    """


    
    def start_gui(self,ok = True):
        """Starts the GUI, if everything ok , to change

        """
        
        if ok:
            self.mainloop()
        else:
            self.master.destroy()

    def createWidgets(self):
        """Create the set of initial widgets.

     

        """
        
        # Create the label

        self.title = tk.Label(
                self, text = " Monitor and Control")
        self.title.grid(
            row=0, column=0,columnspan=6, sticky = tk.E+tk.W )

        self.blankLiner7 = tk.Label(self, text = " ")
        self.blankLiner7.grid(row=6, column=0, columnspan=6, sticky="we")


      
        # Create the top row of six groups

        self.bRow1Col0 = tk.Button(self)
        self.bRow1Col0["text"] = "UPDATE"
        self.bRow1Col0.grid(row=1, column=0)
        self.bRow2Col0 = tk.Button(self)
        self.bRow2Col0["text"] = "GET"
        self.bRow2Col0.grid(row=2, column=0)
        self.eRow3Col0 = tk.Entry(self)
        self.eRow3Col0["width"] = 10
        self.eRow3Col0["justify"]="center"
        self.eRow3Col0.grid(row=3, column=0)
        self.lRow4Col0 = tk.Label(self, text="DHT20 Temp")
        self.lRow4Col0.grid(row=4, column=0)
        self.bRow5Col0 = tk.Button(self)
        self.bRow5Col0["text"] = "SIMULATE"
        self.bRow5Col0.grid(row=5, column=0)

        self.bRow1Col1 = tk.Button(self)
        self.bRow1Col1["text"] = "UPDATE"
        self.bRow1Col1.grid(row=1, column=1)
        self.bRow2Col1 = tk.Button(self)
        self.bRow2Col1["text"] = "GET"
        self.bRow2Col1.grid(row=2, column=1)
        self.eRow3Col1 = tk.Entry(self)
        self.eRow3Col1["width"] = 10
        self.eRow3Col1["justify"]="center"
        self.eRow3Col1.grid(row=3, column=1)
        self.lRow4Col1 = tk.Label(self, text="DHT20 RH")
        self.lRow4Col1.grid(row=4, column=1)
        self.bRow5Col1 = tk.Button(self)
        self.bRow5Col1["text"] = "SIMULATE"
        self.bRow5Col1.grid(row=5, column=1)

        self.bRow1Col2 = tk.Button(self)
        self.bRow1Col2["text"] = "UPDATE"
        self.bRow1Col2.grid(row=1, column=2)
        self.bRow2Col2 = tk.Button(self)
        self.bRow2Col2["text"] = "GET"
        self.bRow2Col2.grid(row=2, column=2)
        self.eRow3Col2 = tk.Entry(self)
        self.eRow3Col2["width"] = 10
        self.eRow3Col2["justify"]="center"
        self.eRow3Col2.grid(row=3, column=2)
        self.lRow4Col2 = tk.Label(self, text="RemLR Temp")
        self.lRow4Col2.grid(row=4, column=2)
        self.bRow5Col2 = tk.Button(self)
        self.bRow5Col2["text"] = "SIMULATE"
        self.bRow5Col2.grid(row=5, column=2)

        self.bRow1Col3 = tk.Button(self)
        self.bRow1Col3["text"] = "UPDATE"
        self.bRow1Col3.grid(row=1, column=3)
        self.bRow2Col3 = tk.Button(self)
        self.bRow2Col3["text"] = "GET"
        self.bRow2Col3.grid(row=2, column=3)
        self.sRow3Col3 = tk.Spinbox(self, from_=50, to=90)
        self.sRow3Col3["width"] = 10
        self.sRow3Col3["justify"]="center"
        self.sRow3Col3.grid(row=3, column=3)
        self.lRow4Col3 = tk.Label(self, text="RemLR RH")
        self.lRow4Col3.grid(row=4, column=3)
        self.bRow5Col3 = tk.Button(self)
        self.bRow5Col3["text"] = "SIMULATE"
        self.bRow5Col3.grid(row=5, column=3)

        self.bRow1Col4 = tk.Button(self)
        self.bRow1Col4["text"] = "UPDATE"
        self.bRow1Col4.grid(row=1, column=4)
        self.bRow2Col4 = tk.Button(self)
        self.bRow2Col4["text"] = "GET"
        self.bRow2Col4.grid(row=2, column=4)
        self.sRow3Col4 = tk.Spinbox(self, from_=50, to=90)
        self.sRow3Col4["width"] = 10
        self.sRow3Col4["justify"]="center"
        self.sRow3Col4.grid(row=3, column=4)
        self.lRow4Col4 = tk.Label(self, text="RemBR Temp")
        self.lRow4Col4.grid(row=4, column=4)
        self.bRow5Col4 = tk.Button(self)
        self.bRow5Col4["text"] = "SIMULATE"
        self.bRow5Col4.grid(row=5, column=4)

        self.bRow1Col5 = tk.Button(self)
        self.bRow1Col5["text"] = "UPDATE"
        self.bRow1Col5.grid(row=1, column=5)
        self.bRow2Col5 = tk.Button(self)
        self.bRow2Col5["text"] = "GET"
        self.bRow2Col5.grid(row=2, column=5)
        self.sRow3Col5 = tk.Spinbox(self, from_=50, to=90)
        self.sRow3Col5["width"] = 10
        self.sRow3Col5["justify"]="center"
        self.sRow3Col5.grid(row=3, column=5)
        self.lRow4Col5 = tk.Label(self, text="RemBR RH")
        self.lRow4Col5.grid(row=4, column=5)
        self.bRow5Col5 = tk.Button(self)
        self.bRow5Col5["text"] = "SIMULATE"
        self.bRow5Col5.grid(row=5, column=5)

        # Create the middle group of six buttons

        self.bRow7Col0 = tk.Button(self)
        self.bRow7Col0["text"] = "UPDATE"
        self.bRow7Col0.grid(row=7, column=0)
        self.bRow8Col0 = tk.Button(self)
        self.bRow8Col0["text"] = "GET"
        self.bRow8Col0.grid(row=8, column=0)
        self.eRow9Col0 = tk.Entry(self)
        self.eRow9Col0["width"] = 10
        self.eRow9Col0["justify"]="center"
        self.eRow9Col0.grid(row=9, column=0)
        self.lRow10Col0 = tk.Label(self, text="ExtTemp")
        self.lRow10Col0.grid(row=10, column=0)
        self.bRow11Col0 = tk.Button(self)
        self.bRow11Col0["text"] = "SIMULATE"
        self.bRow11Col0.grid(row=11, column=0)

        self.bRow7Col1 = tk.Button(self)
        self.bRow7Col1["text"] = "UPDATE"
        self.bRow7Col1.grid(row=7, column=1)
        self.bRow8Col1 = tk.Button(self)
        self.bRow8Col1["text"] = "GET"
        self.bRow8Col1.grid(row=8, column=1)
        self.eRow9Col1 = tk.Entry(self)
        self.eRow9Col1["width"] = 10
        self.eRow9Col1["justify"]="center"
        self.eRow9Col1.grid(row=9, column=1)
        self.lRow10Col1 = tk.Label(self, text="ExtRH")
        self.lRow10Col1.grid(row=10, column=1)
        self.bRow11Col1 = tk.Button(self)
        self.bRow11Col1["text"] = "SIMULATE"
        self.bRow11Col1.grid(row=11, column=1)

        self.bRow7Col2 = tk.Button(self)
        self.bRow7Col2["text"] = "UPDATE"
        self.bRow7Col2.grid(row=7, column=2)
        self.bRow8Col2 = tk.Button(self)
        self.bRow8Col2["text"] = "GET"
        self.bRow8Col2.grid(row=8, column=2)
        self.bRow9Col2 = tk.Spinbox(self, from_=50, to=90)
        self.bRow9Col2["width"] = 10
        self.bRow9Col2["justify"]="center"
        self.bRow9Col2.grid(row=9, column=2)
        self.lRow10Col2 = tk.Label(self, text="LR Set")
        self.lRow10Col2.grid(row=10, column=2)
        self.bRow11Col2 = tk.Button(self)
        self.bRow11Col2["text"] = "SIMULATE"
        self.bRow11Col2.grid(row=11, column=2)

        self.bRow7Col3 = tk.Button(self)
        self.bRow7Col3["text"] = "UPDATE"
        self.bRow7Col3.grid(row=7, column=3)
        self.bRow8Col3 = tk.Button(self)
        self.bRow8Col3["text"] = "GET"
        self.bRow8Col3.grid(row=8, column=3)
        self.bRow9Col3 = tk.Spinbox(self, from_=50, to=90)
        self.bRow9Col3["width"] = 10
        self.bRow9Col3["justify"]="center"
        self.bRow9Col3.grid(row=9, column=3)
        self.lRow10Col3 = tk.Label(self, text="BR Set")
        self.lRow10Col3.grid(row=10, column=3)
        self.bRow11Col3 = tk.Button(self)
        self.bRow11Col3["text"] = "SIMULATE"
        self.bRow11Col3.grid(row=11, column=3)

        self.bRow7Col4 = tk.Button(self)
        self.bRow7Col4["text"] = "UPDATE"
        self.bRow7Col4.grid(row=7, column=4)
        self.bRow8Col4 = tk.Button(self)
        self.bRow8Col4["text"] = "GET"
        self.bRow8Col4.grid(row=8, column=4)
        self.bRow9Col4 = tk.Spinbox(self, from_=50, to=90)
        self.bRow9Col4["width"] = 10
        self.bRow9Col4["justify"]="center"
        self.bRow9Col4.grid(row=9, column=4)
        self.lRow10Col4 = tk.Label(self, text="LRIFeel")
        self.lRow10Col4.grid(row=10, column=4)
        self.bRow11Col4 = tk.Button(self)
        self.bRow11Col4["text"] = "SIMULATE"
        self.bRow11Col4.grid(row=11, column=4)

        self.bRow7Col5 = tk.Button(self)
        self.bRow7Col5["text"] = "UPDATE"
        self.bRow7Col5.grid(row=7, column=5)
        self.bRow8Col5 = tk.Button(self)
        self.bRow8Col5["text"] = "GET"
        self.bRow8Col5.grid(row=8, column=5)
        self.bRow9Col5 = tk.Spinbox(self, from_=50, to=90)
        self.bRow9Col5["width"] = 10
        self.bRow9Col5["justify"]="center"
        self.bRow9Col5.grid(row=9, column=5)
        self.lRow10Col5 = tk.Label(self, text="BRIFeel")
        self.lRow10Col5.grid(row=10, column=5)
        self.bRow11Col5 = tk.Button(self)
        self.bRow11Col5["text"] = "SIMULATE"
        self.bRow11Col5.grid(row=11, column=5)



        # Create the bottom group of six buttons

        self.bRow13Col0 = tk.Button(self)
        self.bRow13Col0["text"] = "UPDATE"
        self.bRow13Col0.grid(row=13, column=0)
        self.bRow14Col0 = tk.Button(self)
        self.bRow14Col0["text"] = "GET"
        self.bRow14Col0.grid(row=14, column=0)
        self.bRow15Col0 = tk.Spinbox(self, from_=50, to=90)
        self.bRow15Col0["width"] = 10
        self.bRow15Col0["justify"]="center"
        self.bRow15Col0.grid(row=15, column=0)
        self.lRow16Col0 = tk.Label(self, text="Gas Relay")
        self.lRow16Col0.grid(row=16, column=0)
        self.bRow17Col0 = tk.Button(self)
        self.bRow17Col0["text"] = "SIMULATE"
        self.bRow17Col0.grid(row=17, column=0)

        self.bRow13Col1 = tk.Button(self)
        self.bRow13Col1["text"] = "UPDATE"
        self.bRow13Col1.grid(row=13, column=1)
        self.bRow14Col1 = tk.Button(self)
        self.bRow14Col1["text"] = "GET"
        self.bRow14Col1.grid(row=14, column=1)
        self.bRow15Col1 = tk.Spinbox(self, from_=50, to=90)
        self.bRow15Col1["width"] = 10
        self.bRow15Col1["justify"]="center"
        self.bRow15Col1.grid(row=15, column=1)
        self.lRow16Col1 = tk.Label(self, text="BR Remo")
        self.lRow16Col1.grid(row=16, column=1)
        self.bRow17Col1 = tk.Button(self)
        self.bRow17Col1["text"] = "SIMULATE"
        self.bRow17Col1.grid(row=17, column=1)

        self.bRow13Col2 = tk.Button(self)
        self.bRow13Col2["text"] = "UPDATE"
        self.bRow13Col2.grid(row=13, column=2)
        self.bRow14Col2 = tk.Button(self)
        self.bRow14Col2["text"] = "GET"
        self.bRow14Col2.grid(row=14, column=2)
        self.bRow15Col2 = tk.Spinbox(self, from_=50, to=90)
        self.bRow15Col2["width"] = 10
        self.bRow15Col2["justify"]="center"
        self.bRow15Col2.grid(row=15, column=2)
        self.lRow16Col2 = tk.Label(self, text="LR Remo")
        self.lRow16Col2.grid(row=16, column=2)
        self.bRow17Col2 = tk.Button(self)
        self.bRow17Col2["text"] = "SIMULATE"
        self.bRow17Col2.grid(row=17, column=2)

        self.bRow13Col3 = tk.Button(self)
        self.bRow13Col3["text"] = "UPDATE"
        self.bRow13Col3.grid(row=13, column=3)
        self.bRow14Col3 = tk.Button(self)
        self.bRow14Col3["text"] = "GET"
        self.bRow14Col3.grid(row=14, column=3)
        self.bRow15Col3 = tk.Spinbox(self, from_=50, to=90)
        self.bRow15Col3["width"] = 10
        self.bRow15Col3["justify"]="center"
        self.bRow15Col3.grid(row=15, column=3)
        self.lRow16Col3 = tk.Label(self, text="RESERVED")
        self.lRow16Col3.grid(row=16, column=3)
        self.bRow17Col3 = tk.Button(self)
        self.bRow17Col3["text"] = "SIMULATE"
        self.bRow17Col3.grid(row=17, column=3)

        self.bRow13Col4 = tk.Button(self)
        self.bRow13Col4["text"] = "UPDATE"
        self.bRow13Col4.grid(row=13, column=4)
        self.bRow14Col4 = tk.Button(self)
        self.bRow14Col4["text"] = "GET"
        self.bRow14Col4.grid(row=14, column=4)
        self.bRow15Col4 = tk.Spinbox(self, from_=50, to=90)
        self.bRow15Col4["width"] = 10
        self.bRow15Col4["justify"]="center"
        self.bRow15Col4.grid(row=15, column=4)
        self.lRow16Col4 = tk.Label(self, text="LR Remo LL")
        self.lRow16Col4.grid(row=16, column=4)
        self.bRow17Col4 = tk.Button(self)
        self.bRow17Col4["text"] = "SIMULATE"
        self.bRow17Col4.grid(row=17, column=4)

        self.bRow13Col5 = tk.Button(self)
        self.bRow13Col5["text"] = "UPDATE"
        self.bRow13Col5.grid(row=13, column=5)
        self.bRow14Col5 = tk.Button(self)
        self.bRow14Col5["text"] = "GET"
        self.bRow14Col5.grid(row=14, column=5)
        self.bRow15Col5 = tk.Spinbox(self, from_=50, to=90)
        self.bRow15Col5["width"] = 10
        self.bRow15Col5["justify"]="center"
        self.bRow15Col5.grid(row=15, column=5)
        self.lRow16Col5 = tk.Label(self, text="BR Remo LL")
        self.lRow16Col5.grid(row=16, column=5)
        self.bRow17Col5 = tk.Button(self)
        self.bRow17Col5["text"] = "SIMULATE"
        self.bRow17Col5.grid(row=17, column=5)


    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        # option is needed to put the main label in the window
        self.createWidgets()
        
    


