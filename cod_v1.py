#Codul sursă al programului
#Stingere ecran, orpire sunet, oprire video și repornire la detectarea
#unui nou input de la telecomandă

import RPi.GPIO as GPIO
import time
import os
from gpiozero import LED
from signal import pause
cmd1 = 'xset -display :0.0 dpms force off'
cmd = 'xset -display :0.0 dpms force on'
mute = 'amixer set Master mute'
unmute= 'amixer set Master unmute'
BackSpace = 'xdotool key BackSpace'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIR_PIN = 23
LED_PIN = 21
IR_PIN = 17 

indicator = LED(LED_PIN)
GPIO.setup(IR_PIN, GPIO.IN)

count = 1

GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.output(LED_PIN,False)

print('Starting up the PIR Module (click on STOP to exit)')
time.sleep(1)
print ('Ready')
start = time.time()
end = time.time()
elapsed= end - start
on=1
while True:
    if GPIO.input(PIR_PIN ):
        print('Motion Detected')
        start = time.time()
        GPIO.output(LED_PIN,True)
        time.sleep(0.5)
        GPIO.output(LED_PIN, False)
        if on== 0 :
            os.system(cmd)
            os.system(unmute)
            os.system(BackSpace)
            on=1
    if (elapsed > 20):
        os.system(cmd1)
        os.system(mute)
        os.system(BackSpace)
        on=0
    GPIO.output(LED_PIN, False)
    end = time.time()
    elapsed = end - start
    
    print(elapsed)
    got_something = GPIO.input(IR_PIN)
    
    if got_something:
        indicator.off()
    else:
        indicator.on()
        print("{:>3} Got something".format(count))
        if on== 0 :
            os.system(cmd)
            os.system(unmute)
            os.system(BackSpace)
            on=1
        start = time.time()
        GPIO.output(LED_PIN,True)
        time.sleep(0.5)
        GPIO.output(LED_PIN,False)
    count += 1
