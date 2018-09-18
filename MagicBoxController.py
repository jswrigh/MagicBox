
from MagicBoxView import MagicBoxView
from MagicBoxDHT22 import MagicBoxDHT22
import MagicBoxQ

class MagicBoxController(object):  


    def nothing(self):
        pass

    def showBoxTemp(self):
        self.s.DHT22()
        self.view.labelOne.configure(text=self.s.tempF)

    def showBoxHumidity(self):
        self.s.DHT22()
        self.view.labelTwo.configure(text=self.s.humidity)

    def showOutTemp(self):
        self.q.readQ()
        self.view.labelThree.configure(text=self.q.data['environment']['outsideTemp'])

    def showIFeel(self):
        self.q.readQ()
        self.view.labelFour.configure(text=self.q.data['settings']['iFeel'])
        

    def init_view(self,root):
        """Initializes GUI view

            In addition it bindes the Buttons with the callback methods.

           
        """
        self.view = MagicBoxView(master=root)   
    
        # Bind buttons with callback methods
        self.view.one["command"] = self.showBoxTemp
        self.view.two["command"] = self.showBoxHumidity
        self.view.three["command"] = self.showOutTemp
        self.view.four["command"] = self.showIFeel

        # Start the gui 
        self.view.start_gui()

    def __init__(self):
        self.s=MagicBoxDHT22()
        self.q=MagicBoxQ.MagicBoxQueue()
        


