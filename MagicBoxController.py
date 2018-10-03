
from MagicBoxView import MagicBoxView
from MagicBoxDHT22 import MagicBoxDHT22
import MagicBoxQ

class MagicBoxController(object):  


    def nothing(self):
        pass

    def showBoxTemp(self):
        self.nowTemp = self.q.updateInsideTemp()
        self.view.labelOne.configure(text=self.nowTemp)

    def showBoxHumidity(self):
        self.nowHumidity = self.q.updateInsideHumidity()
        self.view.labelTwo.configure(text=self.nowHumidity)

    def showOutTemp(self):
        self.nowExtTemp = self.q.updateOutsideTemp()
        self.view.labelThree.configure(text=self.nowExtTemp)

    def showIFeel(self):
        self.q.readQ()
        self.view.labelFour.configure(text=self.q.data['settings']['iFeel'])

    def readSetTemp(self):
        self.q.data['settings']['setTemp']=self.view.bThree.get()
        self.q.writeQ()
        

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
        self.view.bThree["command"] = self.readSetTemp

        # Start the gui 
        self.view.start_gui()

    def __init__(self):
        self.s=MagicBoxDHT22()
        self.q=MagicBoxQ.MagicBoxQueue()
        


