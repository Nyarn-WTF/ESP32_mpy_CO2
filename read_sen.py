import machine
from time import sleep
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
import dht

class Sensors:
    co2sen = machine.UART(2,baudrate = 9600,rx = 33,tx = 25)
    co2sen.init(bits=8,parity=None,stop=1,timeout=1000)
    b = bytearray([0xff, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79])
    dht22 = dht.DHT22(Pin(15))

    parametor = {"templature":0,"humidity":0,"Co2_ppm":0,"THI":0}
    def __init__(self):
        pass

    def Read_Co2(self):
        try:
            self.co2sen.write(self.b)
            sleep(1)
        except:
            pass
        try:
            n = self.co2sen.read()
        except:
            pass
        self.parametor["Co2_ppm"] = n[2]*256+n[3]
    
    def Read_TAH(self):
        self.dht22.measure()
        self.parametor["temprature"] = self.dht22.temperature()
        self.parametor["humidity"]   = self.dht22.humidity()
        self.parametor["THI"]        = 0.81*self.parametor["temprature"]+0.01*self.parametor["humidity"]*(0.99*self.parametor["temprature"]-14.3)+46.3

    def Output(self):
        return self.parametor
    