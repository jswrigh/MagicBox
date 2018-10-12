
from MagicBoxView import MagicBoxView
from MagicBoxDHT22 import MagicBoxDHT22
import MagicBoxQ

class MagicBoxController(object):  


    def nothing(self):
        pass

    def updateBoxTemp(self):
        self.nowTemp = self.q.updateInsideTemp()
        self.view.eRow3Col0.delete(0,10)
        self.view.eRow3Col0["fg"] = "black"
        self.view.eRow3Col0.insert(0,self.nowTemp)

    def getBoxTemp(self):
        self.nowTemp = self.q.getInsideTemp()
        self.view.eRow3Col0.delete(0,10)
        self.view.eRow3Col0.insert(0,self.nowTemp)

    def setBoxTemp(self):
        self.nowTemp = float(self.view.eRow3Col0.get())
        self.q.setInsideTemp(self.nowTemp)
        self.view.eRow3Col0.delete(0,10)
        self.view.eRow3Col0["fg"] = "green"
        self.view.eRow3Col0.insert(0,self.nowTemp)

    def updateBoxRH(self):
        self.nowRh = self.q.updateInsideRh()
        self.view.eRow3Col1.delete(0,10)
        self.view.eRow3Col1["fg"] = "black"
        self.view.eRow3Col1.insert(0,self.nowRh)

    def getBoxRH(self):
        self.nowRh = self.q.getInsideRh()
        self.view.eRow3Col1.delete(0,10)
        self.view.eRow3Col1.insert(0,self.nowRh)

    def setBoxRH(self):
        self.nowRh = float(self.view.eRow3Col1.get())
        self.q.setInsideRh(self.nowRh)
        self.view.eRow3Col1.delete(0,10)
        self.view.eRow3Col1["fg"] = "green"
        self.view.eRow3Col1.insert(0,self.nowRh)

    def updateExtTemp(self):
        self.nowTemp = self.q.updateOutsideTemp()
        self.view.eRow9Col0.delete(0,10)
        self.view.eRow9Col0["fg"] = "black"
        self.view.eRow9Col0.insert(0,self.nowTemp)

    def getExtTemp(self):
        self.nowTemp = self.q.getOutsideTemp()
        self.view.eRow9Col0.delete(0,10)
        self.view.eRow9Col0.insert(0,self.nowTemp)

    def setExtTemp(self):
        self.nowTemp = float(self.view.eRow9Col0.get())
        self.q.setOutsideTemp(self.nowTemp)
        self.view.eRow9Col0.delete(0,10)
        self.view.eRow9Col0["fg"] = "green"
        self.view.eRow9Col0.insert(0,self.nowTemp)

    def updateExtRH(self):
        self.nowRh = self.q.updateOutsideRh()
        self.view.eRow9Col1.delete(0,10)
        self.view.eRow9Col1["fg"] = "black"
        self.view.eRow9Col1.insert(0,self.nowRh)

    def getExtRH(self):
        self.nowRh = self.q.getOutsideRh()
        self.view.eRow9Col1.delete(0,10)
        self.view.eRow9Col1.insert(0,self.nowRh)

    def setExtRH(self):
        self.nowRh = float(self.view.eRow9Col1.get())
        self.q.setOutsideRh(self.nowRh)
        self.view.eRow9Col1.delete(0,10)
        self.view.eRow9Col1["fg"] = "green"
        self.view.eRow9Col1.insert(0,self.nowRh)

    def showRemLrTemp(self): #NEEDS UPDATE
        self.q.readQ()
        self.view.lRow1Col2.configure(text=self.q.data['settings']['iFeel'])

    def showRemLrRH(self): #NEEDS UPDATE
        self.q.readQ()
        self.view.lRow1Col3.configure(text=self.q.data['settings']['iFeel'])

    def showRemBrTemp(self): #NEEDS UPDATE
        self.q.readQ()
        self.view.lRow1Col4.configure(text=self.q.data['settings']['iFeel'])

    def showRemBrRH(self): #NEEDS UPDATE
        self.q.readQ()
        self.view.lRow1Col5.configure(text=self.q.data['settings']['iFeel'])

    def showOutTemp(self):
        self.nowExtTemp = self.q.updateOutsideTemp()
        self.view.lRow2Col0.configure(text=self.nowExtTemp)

    def showOutRH(self): #NEEDS UPDATE
        self.nowExtTemp = self.q.updateOutsideTemp()
        # self.view.lRow2Col1.configure(text=self.nowExtTemp)

    def showLrSetTemp(self): #NEEDS UPDATE
        self.q.readQ()
        self.view.lRow2Col2.configure(text=self.q.data['settings']['iFeel'])

    def showBrSetTemp(self): #NEEDS UPDATE
        self.q.readQ()
        self.view.lRow2Col3.configure(text=self.q.data['settings']['iFeel'])

    def showLrIFeel(self): #NEEDS UPDATE
        self.q.readQ()
        self.view.lRow2Col4.configure(text=self.q.data['settings']['iFeel'])

    def showBrIFeel(self): #NEEDS UPDATE
        self.q.readQ()
        self.view.lRow2Col5.configure(text=self.q.data['settings']['iFeel'])

    def showGasRelay(self): #NEEDS UPDATE
        self.q.readQ()
        self.view.lRow3Col0.configure(text=self.q.data['settings']['iFeel'])

    def showLrRemo(self): #NEEDS UPDATE
        self.q.readQ()
        lrRem=self.view.eRow3Col1.get()
        print(lrRem)
        print(len(lrRem))
        self.view.eRow3Col1.delete(0,len(lrRem))
        self.view.eRow3Col1.insert(0,"68")
        # self.view.lRow3Col1.configure(text=self.q.data['settings']['iFeel'])

    def showBrRemo(self): #NEEDS UPDATE
        self.q.readQ()
        self.view.lRow3Col2.configure(text=self.q.data['settings']['iFeel'])

    def reserved(self): #NEEDS UPDATE
        print("Reserved for future use")
        
    def readSetTemp(self):
        self.q.data['settings']['setTemp']=self.view.bThree.get()
        self.q.writeQ()
        

    def init_view(self,root):
        """Initializes GUI view

            In addition it bindes the Buttons with the callback methods.

           
        """
        self.view = MagicBoxView(master=root)   
    
        # Bind buttons with callback methods
        self.view.bRow1Col0["command"] = self.updateBoxTemp
        self.view.bRow2Col0["command"] = self.getBoxTemp
        self.view.bRow5Col0["command"] = self.setBoxTemp
        self.view.bRow1Col1["command"] = self.updateBoxRH
        self.view.bRow2Col1["command"] = self.getBoxRH
        self.view.bRow5Col1["command"] = self.setBoxRH
        self.view.bRow7Col0["command"] = self.updateExtTemp
        self.view.bRow8Col0["command"] = self.getExtTemp
        self.view.bRow11Col0["command"] = self.setExtTemp
        self.view.bRow7Col1["command"] = self.updateExtRH
        self.view.bRow8Col1["command"] = self.getExtRH
        self.view.bRow11Col1["command"] = self.setExtRH
#        self.view.bRow1Col2["command"] = self.showRemLrTemp
#        self.view.bRow1Col3["command"] = self.showRemLrRH
#        self.view.bRow1Col4["command"] = self.showRemBrTemp
#        self.view.bRow1Col5["command"] = self.showRemBrRH

#        self.view.bRow2Col0["command"] = self.showOutTemp
#        self.view.bRow2Col1["command"] = self.showOutRH
#        self.view.bRow2Col2["command"] = self.showLrSetTemp
#        self.view.bRow2Col3["command"] = self.showBrSetTemp
#        self.view.bRow2Col4["command"] = self.showLrIFeel
#        self.view.bRow2Col5["command"] = self.showBrIFeel
        
#        self.view.eRow3Col0["command"] = self.showGasRelay
#        self.view.bRow2Col1["command"] = self.showLrRemo
#        self.view.sRow3Col2["command"] = self.showBrRemo
#        self.view.sRow3Col3["command"] = self.reserved
#        self.view.sRow3Col4["command"] = self.reserved
#        self.view.sRow3Col5["command"] = self.reserved
        
#        self.view.bThree["command"] = self.readSetTemp

        # Start the gui 
        self.view.start_gui()

    def __init__(self):
        self.s=MagicBoxDHT22()
        self.q=MagicBoxQ.MagicBoxQueue()
