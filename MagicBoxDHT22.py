import time
import DHT22
import pigpio
import Sensor

class MagicBoxDHT22(object):

    def DHT22(self):
        self.s.trigger()
        time.sleep(0.2)
        self.tempF=round(self.s.temperature()*1.8+32,2) #+adjustment
        self.humidity=round(self.s.humidity())

    def __init__(self):
        self.pi=pigpio.pi()
        self.s=DHT22.sensor(self.pi, 4)
        self.tempF=0
        self.humidity=0
        # test code #
        self.s.trigger()
        time.sleep(0.2)
        print(self.s.temperature())
