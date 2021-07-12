import time
import RPi.GPIO as GPIO

rightFrontForward = 26
rightBackForward = 5
leftFrontForward = 16
leftBackForward = 12

rightFrontBackward = 20
rightBackBackward = 13
leftFrontBackward = 19
leftBackBackward = 6

enable = 21

runTime = 1
waitTime = 2
turnTime = 0.25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(rightFrontForward, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(rightBackForward, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(leftFrontForward, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(leftBackForward, GPIO.OUT, initial = GPIO.LOW)

GPIO.setup(rightFrontBackward, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(rightBackBackward, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(leftFrontBackward, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(leftBackBackward, GPIO.OUT, initial = GPIO.LOW)

GPIO.setup(enable, GPIO.OUT, initial = GPIO.HIGH)

def offMotors():
    GPIO.output(rightFrontForward, GPIO.LOW)
    GPIO.output(leftFrontForward, GPIO.LOW)
    GPIO.output(rightBackForward, GPIO.LOW)
    GPIO.output(leftBackForward, GPIO.LOW)

    GPIO.output(rightFrontBackward, GPIO.LOW)
    GPIO.output(leftFrontBackward, GPIO.LOW)
    GPIO.output(rightBackBackward, GPIO.LOW)
    GPIO.output(leftBackBackward, GPIO.LOW)

def test(inputRunTime):
    GPIO.output(rightFrontForward, GPIO.HIGH)
    time.sleep(inputRunTime)
    GPIO.output(leftFrontForward, GPIO.HIGH)
    time.sleep(inputRunTime)
    GPIO.output(leftBackForward, GPIO.HIGH)
    time.sleep(inputRunTime)
    GPIO.output(rightBackForward, GPIO.HIGH)
    time.sleep(2 * inputRunTime)
    print("Forward")

    GPIO.output(rightFrontForward, GPIO.LOW)
    GPIO.output(leftFrontForward, GPIO.LOW)
    GPIO.output(leftBackForward, GPIO.LOW)
    GPIO.output(rightBackForward, GPIO.LOW)
    print("Motors OFF")

    GPIO.output(rightFrontBackward, GPIO.HIGH)
    time.sleep(inputRunTime)
    GPIO.output(leftFrontBackward, GPIO.HIGH)
    time.sleep(inputRunTime)
    GPIO.output(leftBackBackward, GPIO.HIGH)
    time.sleep(inputRunTime)
    GPIO.output(rightBackBackward, GPIO.HIGH)
    time.sleep((2 * inputRunTime))
    print("Backward")

    GPIO.output(rightFrontBackward, GPIO.LOW)
    GPIO.output(leftFrontBackward, GPIO.LOW)
    GPIO.output(leftBackBackward, GPIO.LOW)
    GPIO.output(rightBackBackward, GPIO.LOW)
    print("Motors OFF")

def forward(inputRunTime):
    GPIO.output(rightFrontForward, GPIO.HIGH)
    GPIO.output(leftFrontForward, GPIO.HIGH)
    GPIO.output(leftBackForward, GPIO.HIGH)
    GPIO.output(rightBackForward, GPIO.HIGH)

    print("Moving Forward")
    time.sleep(inputRunTime)
    offMotors()

def backward(inputRunTime):
    GPIO.output(rightFrontBackward, GPIO.HIGH)
    GPIO.output(leftFrontBackward, GPIO.HIGH)
    GPIO.output(rightBackBackward, GPIO.HIGH)
    GPIO.output(leftBackBackward, GPIO.HIGH)
    
    print("Moving Backward")
    time.sleep(inputRunTime)
    offMotors()
    
def left(turnTime):
    GPIO.output(rightFrontForward, GPIO.HIGH)
    GPIO.output(rightBackForward, GPIO.HIGH)
    GPIO.output(leftFrontBackward, GPIO.HIGH)
    GPIO.output(leftBackBackward, GPIO.HIGH)
    
    print("Turning Left")
    time.sleep(turnTime)
    offMotors()

def right(turnTime):
    GPIO.output(leftFrontForward, GPIO.HIGH)
    GPIO.output(leftBackForward, GPIO.HIGH)
    GPIO.output(rightFrontBackward, GPIO.HIGH)
    GPIO.output(rightBackBackward, GPIO.HIGH)
    
    print("Turning Right")
    time.sleep(turnTime)
    offMotors()

def wait():
    print("Waiting")
    time.sleep(waitTime)

try:
    # while(GPIO.HIGH):
    #     forward(runTime)
    #     wait(waitTime)
    #     right(turnTime)

    forward(runTime)
    wait()
    right(turnTime)
    wait()
    left(turnTime)
    wait()
    backward(runTime)


except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()