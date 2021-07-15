import time
import RPi.GPIO as GPIO

rightFront_Forward = 20
rightBack_Forward = 16
leftFront_Forward = 13
leftBack_Forward = 6

rightFront_Backward = 26
rightBack_Backward = 19
leftFront_Backward = 5
leftBack_Backward = 12

enable = 21

runTime = 2
waitTime = 2
turnTime = 0.5

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(rightFront_Forward, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(rightBack_Forward, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(leftFront_Forward, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(leftBack_Forward, GPIO.OUT, initial = GPIO.LOW)

    GPIO.setup(rightFront_Backward, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(rightBack_Backward, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(leftFront_Backward, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(leftBack_Backward, GPIO.OUT, initial = GPIO.LOW)

    GPIO.setup(enable, GPIO.OUT, initial = GPIO.HIGH)

def offMotors():
    GPIO.output(rightFront_Forward, GPIO.LOW)
    GPIO.output(leftFront_Forward, GPIO.LOW)
    GPIO.output(rightBack_Forward, GPIO.LOW)
    GPIO.output(leftBack_Forward, GPIO.LOW)

    GPIO.output(rightFront_Backward, GPIO.LOW)
    GPIO.output(leftFront_Backward, GPIO.LOW)
    GPIO.output(rightBack_Backward, GPIO.LOW)
    GPIO.output(leftBack_Backward, GPIO.LOW)

def transistorTest():
    GPIO.setup(4, GPIO.OUT, initial = GPIO.LOW)
    GPIO.output(4, GPIO.HIGH)
    wait(waitTime)

def motorTest():
    GPIO.output(rightFront_Forward, GPIO.HIGH)
    wait(waitTime)
    GPIO.output(rightBack_Forward, GPIO.HIGH) 
    wait(waitTime)
    GPIO.output(leftFront_Forward, GPIO.HIGH)
    wait(waitTime)
    GPIO.output(leftBack_Forward, GPIO.HIGH)
    wait(waitTime)

    offMotors()

    GPIO.output(rightFront_Backward, GPIO.HIGH)
    wait(waitTime)
    GPIO.output(rightBack_Backward, GPIO.HIGH) 
    wait(waitTime)
    GPIO.output(leftFront_Backward, GPIO.HIGH)
    wait(waitTime)
    GPIO.output(leftBack_Backward, GPIO.HIGH)
    wait(waitTime)

def movementTest():
    moveForward(runTime)
    wait(waitTime)
    moveBackward(runTime)
    wait(waitTime)
    turnRight(turnTime)
    wait(waitTime)
    turnLeft(turnTime)
    wait(waitTime)
    moveRight(runTime)
    wait(waitTime)
    moveLeft(runTime)

def PWMtest():
    p = GPIO.PWM(enable, 500)
    p.start(0)

    for i in range(0, 101):
        p.ChangeDutyCycle(i)
        print(i)
        moveForward(0.1)

def moveForward(inputRunTime):
    GPIO.output(rightFront_Forward, GPIO.HIGH)
    GPIO.output(leftFront_Forward, GPIO.HIGH)
    GPIO.output(leftBack_Forward, GPIO.HIGH)
    GPIO.output(rightBack_Forward, GPIO.HIGH)

    print("Moving Forward")
    time.sleep(inputRunTime)
    offMotors()

def moveBackward(inputRunTime):
    GPIO.output(rightFront_Backward, GPIO.HIGH)
    GPIO.output(leftFront_Backward, GPIO.HIGH)
    GPIO.output(rightBack_Backward, GPIO.HIGH)
    GPIO.output(leftBack_Backward, GPIO.HIGH)
    
    print("Moving Backward")
    time.sleep(inputRunTime)
    offMotors()
    
def turnRight(inputTurnTime):
    GPIO.output(leftFront_Forward, GPIO.HIGH)
    GPIO.output(leftBack_Forward, GPIO.HIGH)
    GPIO.output(rightFront_Backward, GPIO.HIGH)
    GPIO.output(rightBack_Backward, GPIO.HIGH)
    
    print("Turning Right")
    time.sleep(inputTurnTime)
    offMotors()

def turnLeft(inputTurnTime):
    GPIO.output(rightFront_Forward, GPIO.HIGH)
    GPIO.output(rightBack_Forward, GPIO.HIGH)
    GPIO.output(leftFront_Backward, GPIO.HIGH)
    GPIO.output(leftBack_Backward, GPIO.HIGH)
    
    print("Turning Left")
    time.sleep(inputTurnTime)
    offMotors()

def moveRight(inputTurnTime):
    GPIO.output(rightBack_Forward, GPIO.HIGH)
    GPIO.output(leftFront_Forward, GPIO.HIGH)
    GPIO.output(rightFront_Backward, GPIO.HIGH)
    GPIO.output(leftBack_Backward, GPIO.HIGH)
    
    print("Moving Right")
    time.sleep(inputTurnTime)
    offMotors()

def moveLeft(inputTurnTime):
    GPIO.output(rightFront_Forward, GPIO.HIGH)
    GPIO.output(leftBack_Forward, GPIO.HIGH)
    GPIO.output(rightBack_Backward, GPIO.HIGH)
    GPIO.output(leftFront_Backward, GPIO.HIGH)
    
    print("Moving Left")
    time.sleep(inputTurnTime)
    offMotors()

def wait(inputWaitTime):
    print("Waiting")
    time.sleep(inputWaitTime)

try:
    setup() 
    motorTest()
    PWMtest()

    # while True:
    #     moveRight(runTime)
    #     moveLeft(runTime)

except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()