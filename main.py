import time
import RPi.GPIO as GPIO

frontRightForward = 26
frontLeftForward = 16
backRightForward = 5
backLeftForward = 12

frontRightBackward = 20
frontLeftBackward = 19
backRightBackward = 13
backLeftBackward = 6

enable = 21

runTime = 1
waitTime = 1
turnTime = 1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(frontRightForward, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(frontLeftForward, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(backLeftForward, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(backRightForward, GPIO.OUT, initial = GPIO.LOW)

GPIO.setup(frontRightBackward, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(frontLeftBackward, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(backRightBackward, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(backLeftBackward, GPIO.OUT, initial = GPIO.LOW)

GPIO.setup(enable, GPIO.OUT, initial = GPIO.HIGH)

def test(inputRunTime):
    GPIO.output(frontRightForward, GPIO.HIGH)
    time.sleep(inputRunTime)
    GPIO.output(frontLeftForward, GPIO.HIGH)
    time.sleep(inputRunTime)
    GPIO.output(backLeftForward, GPIO.HIGH)
    time.sleep(inputRunTime)
    GPIO.output(backRightForward, GPIO.HIGH)
    time.sleep(2 * inputRunTime)
    print("Forward")

    GPIO.output(frontRightForward, GPIO.LOW)
    GPIO.output(frontLeftForward, GPIO.LOW)
    GPIO.output(backLeftForward, GPIO.LOW)
    GPIO.output(backRightForward, GPIO.LOW)
    print("Motors OFF")

    GPIO.output(frontRightBackward, GPIO.HIGH)
    time.sleep(inputRunTime)
    GPIO.output(frontLeftBackward, GPIO.HIGH)
    time.sleep(inputRunTime)
    GPIO.output(backLeftBackward, GPIO.HIGH)
    time.sleep(inputRunTime)
    GPIO.output(backRightBackward, GPIO.HIGH)
    time.sleep((2 * inputRunTime))
    print("Backward")

    GPIO.output(frontRightBackward, GPIO.LOW)
    GPIO.output(frontLeftBackward, GPIO.LOW)
    GPIO.output(backLeftBackward, GPIO.LOW)
    GPIO.output(backRightBackward, GPIO.LOW)
    print("Motors OFF")

def forward(inputRunTime):
    GPIO.output(frontRightBackward, GPIO.HIGH)
    GPIO.output(frontLeftBackward, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(inputRunTime)
    GPIO.output(frontRightBackward, GPIO.LOW)
    GPIO.output(frontLeftBackward, GPIO.LOW)

def reverse(inputRunTime):
    GPIO.output(frontRightForward, GPIO.HIGH)
    GPIO.output(frontLeftForward, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(inputRunTime)
    GPIO.output(frontRightForward, GPIO.LOW)
    GPIO.output(frontLeftForward, GPIO.LOW)
    
def left(inputRunTime):
    GPIO.output(frontRightBackward, GPIO.HIGH)
    GPIO.output(frontLeftForward, GPIO.HIGH)
    print("Turning Right")
    time.sleep(inputRunTime)
    GPIO.output(frontRightBackward, GPIO.LOW)
    GPIO.output(frontLeftForward, GPIO.LOW)

def right(inputRunTime):
    GPIO.output(frontRightForward, GPIO.HIGH)
    GPIO.output(frontLeftBackward, GPIO.HIGH)
    print("Turning Left")
    time.sleep(inputRunTime)
    GPIO.output(frontRightForward, GPIO.LOW)
    GPIO.output(frontLeftBackward, GPIO.LOW)

def wait(inputRunTime):
    print("Waiting")
    time.sleep(inputRunTime)

try:
    # while(GPIO.HIGH):
    #     forward(runTime)
    #     wait(waitTime)
    #     right(turnTime)
    test(1)
    # forward(runTime)
    # wait(waitTime)
    # right(turnTime)

except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()