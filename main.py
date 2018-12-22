import machine
from time import sleep
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C

def main():
    co2sen = machine.UART(2,baudrate = 9600,rx = 33,tx = 25)
    i2c = I2C(scl = Pin(22),sda = Pin(21))
    oled = SSD1306_I2C(128,64,i2c)
    co2sen.init(bits=8,parity=None,stop=1,timeout=1000)
    b = bytearray([0xff, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79])
    oled.text("test",0,0)
    oled.show()
    sleep(1)
    oled.fill(0)
    oled.show()
    while 1:
        co2sen.write(b)
        sleep(1)
        n = co2sen.read()
        if n != None:
            oled.fill(0)
            co2ppm = n[2]*256+n[3]
            oled.text("CO2 : "+str(co2ppm)+"ppm",0,20)
            oled.show()        
        else:            
            oled.fill(0)            
            oled.text("ERR",0,20)            
            oled.show()        
            #sleep(2)
        if __name__ == '__main__':
            main()
