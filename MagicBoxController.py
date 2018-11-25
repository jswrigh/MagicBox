
from MagicBoxView import MagicBoxView
from MagicBoxDHT22 import MagicBoxDHT22
import MagicBoxQ
import time
import automationhat

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

    def updateRemLrTemp(self):
        self.nowTemp = self.q.updateRemoData('Sandi Living Room','te')
        self.view.eRow3Col2.delete(0,10)
        self.view.eRow3Col2["fg"] = "black"
        self.view.eRow3Col2.insert(0,self.nowTemp)

    def getRemLrTemp(self):
        self.nowTemp = self.q.getRemoData('Sandi Living Room','te')
        self.view.eRow3Col2.delete(0,10)
        self.view.eRow3Col2.insert(0,self.nowTemp)

    def setRemLrTemp(self):
        self.nowTemp = float(self.view.eRow3Col2.get())
        self.q.setRemoData('Sandi Living Room','te', self.nowTemp)
        self.view.eRow3Col2.delete(0,10)
        self.view.eRow3Col2["fg"] = "green"
        self.view.eRow3Col2.insert(0,self.nowTemp)

    def updateRemLrIl(self):
        self.nowLight = self.q.updateRemoData('Sandi Living Room','il')
        self.view.eRow3Col3.delete(0,10)
        self.view.eRow3Col3["fg"] = "black"
        self.view.eRow3Col3.insert(0,self.nowLight)

    def getRemLrIl(self):
        self.nowLight = self.q.getRemoData('Sandi Living Room','il')
        self.view.eRow3Col3.delete(0,10)
        self.view.eRow3Col3.insert(0,self.nowLight)

    def setRemLrIl(self):
        self.nowLight = float(self.view.eRow3Col3.get())
        self.q.setRemoData('Sandi Living Room','il', self.nowLight)
        self.view.eRow3Col3.delete(0,10)
        self.view.eRow3Col3["fg"] = "green"
        self.view.eRow3Col3.insert(0,self.nowLight)

    def updateRemBrTemp(self):
        self.nowTemp = self.q.updateRemoData('Sandi Bedroom','te')
        self.view.eRow3Col4.delete(0,10)
        self.view.eRow3Col4["fg"] = "black"
        self.view.eRow3Col4.insert(0,self.nowTemp)

    def getRemBrTemp(self):
        self.nowTemp = self.q.getRemoData('Sandi Bedroom','te')
        self.view.eRow3Col4.delete(0,10)
        self.view.eRow3Col4.insert(0,self.nowTemp)

    def setRemBrTemp(self):
        self.nowTemp = float(self.view.eRow3Col4.get())
        self.q.setRemoData('Sandi Bedroom','te', self.nowTemp)
        self.view.eRow3Col4.delete(0,10)
        self.view.eRow3Col4["fg"] = "green"
        self.view.eRow3Col4.insert(0,self.nowTemp)

    def updateRemBrIl(self):
        self.nowLight = self.q.updateRemoData('Sandi Bedroom','il')
        self.view.eRow3Col5.delete(0,10)
        self.view.eRow3Col5["fg"] = "black"
        self.view.eRow3Col5.insert(0,self.nowLight)

    def getRemBrIl(self):
        self.nowLight = self.q.getRemoData('Sandi Bedroom','il')
        self.view.eRow3Col5.delete(0,10)
        self.view.eRow3Col5.insert(0,self.nowLight)

    def setRemBrIl(self):
        self.nowLight = float(self.view.eRow3Col5.get())
        self.q.setRemoData('Sandi Bedroom','il', self.nowLight)
        self.view.eRow3Col5.delete(0,10)
        self.view.eRow3Col5["fg"] = "green"
        self.view.eRow3Col5.insert(0,self.nowLight)

    def updateGasRelay(self):
        self.gr = self.view.sRow15Col0.get()
        print(self.gr)
        if self.gr == "ON":
            automationhat.relay.one.off()
        elif self.gr == "OFF":
            automationhat.relay.one.on()
        self.q.setGasRelay(self.gr)
        
    def getGasRelay(self):
        self.gr = self.q.getGasRelay()
        self.view.sRow15Col0.delete(0,10)
        self.view.sRow15Col0.insert(0,self.gr)
        
    def getRemBrCmd(self):
        self.lastCommand = self.q.getLastRemoCmd('brRemoCommand')
        self.view.sRow15Col1.delete(0,10)
        self.view.sRow15Col1.insert(0,self.lastCommand)
        
    def getRemLrCmd(self):
        self.lastCommand = self.q.getLastRemoCmd('lrRemoCommand')
        self.view.sRow15Col2.delete(0,10)
        self.view.sRow15Col2.insert(0,self.lastCommand)
        
    def updateRemoSignals(self):
        self.q.updateRemoSignals()

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
        self.view.bRow1Col2["command"] = self.updateRemLrTemp
        self.view.bRow2Col2["command"] = self.getRemLrTemp
        self.view.bRow5Col2["command"] = self.setRemLrTemp
        self.view.bRow1Col3["command"] = self.updateRemLrIl
        self.view.bRow2Col3["command"] = self.getRemLrIl
        self.view.bRow5Col3["command"] = self.setRemLrIl
        self.view.bRow1Col4["command"] = self.updateRemBrTemp
        self.view.bRow2Col4["command"] = self.getRemBrTemp
        self.view.bRow5Col4["command"] = self.setRemBrTemp
        self.view.bRow1Col5["command"] = self.updateRemBrIl
        self.view.bRow2Col5["command"] = self.getRemBrIl
        self.view.bRow5Col5["command"] = self.setRemBrIl
        self.view.bRow13Col0["command"] = self.updateGasRelay
        self.view.bRow14Col0["command"] = self.getGasRelay
        self.view.bRow14Col1["command"] = self.getRemBrCmd
        self.view.bRow14Col2["command"] = self.getRemLrCmd

        self.view.bRow13Col5["command"] = self.updateRemoSignals
        
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
