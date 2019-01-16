import machine
from time import sleep
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
import read_sen


i2c = I2C(scl = Pin(22),sda = Pin(21))
oled = SSD1306_I2C(128,64,i2c)
sensors = read_sen.Sensors()

def init():
    oled.text("hello,world!",0,20)
    oled.show()
    sleep(1)
    oled.fill(0)
    oled.show()

def show(co2,temp,humid,thi):
    if co2 != None:
        oled.fill(0)
        oled.text("CO2 : "+str(co2)+"ppm",0,20)
        oled.text("TMP : "+str(temp)+"C",0,30)
        oled.text("HMD : "+str(humid)+"%",0,40)
        oled.text("THI : "+str(thi),0,50)
        if co2 > 2000:
            oled.text("!ATTENTION!",0,0)
            oled.text("Ventilate now!",0,10)
        oled.show()        
    else:            
        oled.fill(0)            
        oled.text("ERR",0,20)            
        oled.show()      

def main():
    init()
    while 1:
        sensors.Read_Co2()
        sensors.Read_TAH()
        param = sensors.Output()
        show(param["Co2_ppm"],param["templature"],param["humidity"],param["THI"])

if __name__ == '__main__':
    main()
