import RPi.GPIO as GPIO
import time
d=[0.97,1.22,1.13,0.9,1.87]
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
    h0=readcount(17,4)
    h1=readcount(26,19)
    h2=readcount(25,24)
    h3=readcount(27,22)
    h4=readcount(16,20)
    time.sleep(10)
    hh0=readcount(17,4)
    hh1=readcount(26,19)
    hh2=readcount(25,24)
    hh3=readcount(27,22)
    hh4=readcount(16,20)

    print("0号桶重量:",-round(((hh0-h0)/1000)/d[0]),"g")
    print("1号桶重量:",-round(((hh1-h1)/1000)/d[1]),"g")
    print("2号桶重量:",-round(((hh2-h2)/1000)/d[2]),"g")
    print("3号桶重量:",-round(((hh3-h3)/1000)/d[3]),"g")
    print("4号桶重量:",round(((hh4-h4)/1000)/d[4]),"g")




