import sys
import time
import RPi.GPIO as GPIO

OUT1 = 19
OUT2 = 16
OUT3 = 26
OUT4 = 20
runTime = 0.75
waitTime = 0.1
turnTime = 0.25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(OUT1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(OUT2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(OUT3, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(OUT4, GPIO.OUT, initial = GPIO.LOW)

def forward(inputRunTime):
    GPIO.output(OUT2, GPIO.HIGH)
    GPIO.output(OUT3, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(inputRunTime)
    GPIO.output(OUT2, GPIO.LOW)
    GPIO.output(OUT3, GPIO.LOW)

def reverse(inputRunTime):
    GPIO.output(OUT1, GPIO.HIGH)
    GPIO.output(OUT4, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(inputRunTime)
    GPIO.output(OUT1, GPIO.LOW)
    GPIO.output(OUT4, GPIO.LOW)
    
def left(inputRunTime):
    GPIO.output(OUT2, GPIO.HIGH)
    GPIO.output(OUT4, GPIO.HIGH)
    print("Turning Right")
    time.sleep(inputRunTime)
    GPIO.output(OUT2, GPIO.LOW)
    GPIO.output(OUT4, GPIO.LOW)

def right(inputRunTime):
    GPIO.output(OUT1, GPIO.HIGH)
    GPIO.output(OUT3, GPIO.HIGH)
    print("Turning Left")
    time.sleep(inputRunTime)
    GPIO.output(OUT1, GPIO.LOW)
    GPIO.output(OUT3, GPIO.LOW)

def wait(inputRunTime):
    print("Waiting")
    time.sleep(inputRunTime)

try:
    # while(GPIO.HIGH):
    #     forward(runTime)
    #     wait(waitTime)
    #     right(turnTime)

    forward(runTime)
    wait(waitTime)
    right(turnTime)

except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()