import RPi.GPIO as GPIO
import time
import os
from gpiozero import LED
from signal import pause
cmd = 'sudo shutdown now'


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIR = 23
LED = 21

indicator = LED(LED)

count = 1

GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED,GPIO.OUT)

time.sleep(1)

start = time.time()
end = time.time()
elapsed= end - start

while True:
    if GPIO.input(PIR):
        start = time.time()
        GPIO.output(LED,True)
        time.sleep(0.5)
    
    if (elapsed > 180):
        os.system(cmd)
    
    GPIO.output(LED, False)
    end = time.time()
    elapsed = end - start
    
    count += 1