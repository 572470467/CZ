import RPi.GPIO as GPIO
import time
list=[(8508,0.98),(8485,1.22),(8501,1.14),(8498.5,0.9),(8588,1.87)]
def readcount(DT,SCK):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DT,GPIO.IN)
    GPIO.setup(SCK,GPIO.OUT,initial=0)
    count=0
    GPIO.setup(DT,GPIO.OUT)
    GPIO.output(DT,1)
    GPIO.output(SCK,0)
    GPIO.setup(DT,GPIO.IN)
    while GPIO.input(DT) ==1:
        pass
    for i in range(24):
        GPIO.output(SCK,1)
        GPIO.output(SCK,0)
        count = (count << 1) | GPIO.input(DT)
    GPIO.output(SCK,1)
    GPIO.output(SCK,0)
    if (count&(1<<(24-1)))!=0:
        count=count-(1<<24)
    count=count^0x800000
    return count
if __name__=='__main__':
    count0=readcount(17,4)
    count1=readcount(26,19)
    count2=readcount(25,24)
    count3=readcount(27,22)
    count4=readcount(16,20)
    #count5=readcount(13,6)                                                                                                                                                                                 
    print("0号桶重量:",-round((count0/1000+list[0][0])/list[0][1]),"g")
    print("1号桶重量:",-round((count1/1000+list[1][0])/list[1][1]),"g")
    print("2号桶重量:",-round((count2/1000+list[2][0])/list[2][1]),"g")
    print("3号桶重量:",-round((count3/1000+list[3][0])/list[3][1]),"g")
    print("4号桶重量:",round((count4/1000-list[4][0])/list[4][1]),"g")
    #print("5号桶重量:",-round((count5/1000)),"g")                                                                                                                                                          


