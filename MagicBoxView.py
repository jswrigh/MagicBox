#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import tkinter as tk
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
                self, text = " What's up ?")
        self.title.grid(
            row=0, column=0,columnspan=4, sticky = tk.E+tk.W )

      
        # Create the top row of four buttons

        self.one = tk.Button(self)
        self.one["text"] = "Current Temp"
        self.one.grid(row=1, column=0)

        self.labelOne = tk.Label(self, text="Temp")
        self.labelOne.grid(row=2, column=0)

        self.two = tk.Button(self)
        self.two["text"] = "Current R.H."
        self.two.grid(row=1, column=1)
     
        self.labelTwo = tk.Label(self, text="RelHum")
        self.labelTwo.grid(row=2, column=1)

        self.three = tk.Button(self)
        self.three["text"] = "ExtTemp"
        self.three.grid(row=1, column=2)

        self.labelThree = tk.Label(self, text="ExtTemp")
        self.labelThree.grid(row=2, column=2)

        self.four = tk.Button(self)
        self.four["text"] = "IFeel"
        self.four.grid(row=1, column=3)

        self.labelFour = tk.Label(self, text="IFeel")
        self.labelFour.grid(row=2, column=3)

        # Create the bottom row of four buttons

        self.bOne = tk.Button(self)
        self.bOne["text"] = "Current Temp"
        self.bOne.grid(row=4, column=0)

        self.labelBOne = tk.Label(self, text="Temp")
        self.labelBOne.grid(row=5, column=0)

        self.bTwo = tk.Button(self)
        self.bTwo["text"] = "Current R.H."
        self.bTwo.grid(row=4, column=1)
     
        self.labelBTwo = tk.Label(self, text="RelHum")
        self.labelBTwo.grid(row=5, column=1)

        self.bThree = tk.Spinbox(self, from_=50, to=90)
        self.bThree["width"] = 10
        self.bThree["justify"]="center"
        self.bThree.grid(row=4, column=2)

        self.labelBThree = tk.Label(self, text="ExtTemp")
        self.labelBThree.grid(row=5, column=2)

        self.bFour = tk.Button(self)
        self.bFour["text"] = "IFeel"
        self.bFour.grid(row=4, column=3)

        self.labelBFour = tk.Label(self, text="IFeel")
        self.labelBFour.grid(row=5, column=3)


    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        # option is needed to put the main label in the window
        self.createWidgets()
        
    


