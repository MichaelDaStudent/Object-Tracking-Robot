#include "Movement.h"
#define SECONDS_TO_MICRO * 1000000

namespace Movement
{
    float runTime = 1 SECONDS_TO_MICRO;
    float waitTime = 1 SECONDS_TO_MICRO;
    float turnTime = 0.2 SECONDS_TO_MICRO;
    
    const int rightFront_Forward = 26;
    const int rightBack_Forward = 6;
    const int leftFront_Forward = 16;
    const int leftBack_Forward = 5;
    
    const int rightFront_Backward = 20;
    const int rightBack_Backward = 12;
    const int leftFront_Backward = 16;
    const int leftBack_Backward = 5;
    
    const int enable = 25;

    void setup()
    {
        gpioInitialise();

        gpioSetMode(rightFront_Forward, PI_OUTPUT);
        gpioSetMode(rightBack_Forward, PI_OUTPUT);
        gpioSetMode(leftFront_Forward, PI_OUTPUT);
        gpioSetMode(leftBack_Forward, PI_OUTPUT);

        gpioSetMode(rightFront_Backward, PI_OUTPUT);
        gpioSetMode(rightBack_Backward, PI_OUTPUT);
        gpioSetMode(leftFront_Backward, PI_OUTPUT);
        gpioSetMode(leftBack_Backward, PI_OUTPUT);
        gpioSetMode(enable, PI_OUTPUT);

        offMotors();
        gpioSetPWMrange(enable, 100);
        gpioPWM(enable, 100);
    }

    void cleanup()
    {
        offMotors();
        gpioTerminate();
    }

    void offMotors()
    {
        gpioWrite(rightFront_Forward, 0);
        gpioWrite(rightBack_Forward, 0);
        gpioWrite(leftFront_Forward, 0);
        gpioWrite(leftBack_Forward, 0);

        gpioWrite(rightFront_Backward, 0);
        gpioWrite(rightBack_Backward, 0);
        gpioWrite(leftFront_Backward, 0);
        gpioWrite(leftBack_Backward, 0);
    }

    void motorTest()
    {
        gpioWrite(rightFront_Forward, 1);
        wait(runTime);
        gpioWrite(rightBack_Forward, 1);
        wait(runTime);
        gpioWrite(leftFront_Forward, 1);
        wait(runTime);
        gpioWrite(leftBack_Forward, 1);
        wait(runTime);

        offMotors();

        gpioWrite(rightFront_Backward, 1);
        wait(runTime);
        gpioWrite(rightBack_Backward, 1);
        wait(runTime);
        gpioWrite(leftFront_Backward, 1);
        wait(runTime);
        gpioWrite(leftBack_Backward, 1);
        wait(runTime);
    }

    void movementTest()
    {
        moveForward(runTime);
        wait(waitTime);
        moveBackward(runTime);
        wait(waitTime);
        turnRight(turnTime);
        wait(waitTime);
        turnLeft(turnTime);
        wait(waitTime);
        moveRight(runTime);
        wait(waitTime);
        moveLeft(runTime);
    }

    void PWMtest()
    {
        gpioPWM(enable, 0);

        for(int i = 1; i <= 100; i ++)
        {
            gpioPWM(enable, i);
            printf("%d ", i);
            moveForward(0.1 SECONDS_TO_MICRO);
        }
    }

    void moveForward(int inputRunTime)
    {
        gpioWrite(rightFront_Forward, 1);
        gpioWrite(leftFront_Forward, 1);
        gpioWrite(leftBack_Forward, 1);
        gpioWrite(rightBack_Forward, 1);

        printf("Moving Forward\n");
        gpioDelay(inputRunTime);
        offMotors();
    }

    void moveBackward(int inputRunTime)
    {
        gpioWrite(rightFront_Backward, 1);
        gpioWrite(leftFront_Backward, 1);
        gpioWrite(rightBack_Backward, 1);
        gpioWrite(leftBack_Backward, 1);
        
        printf("Moving Backward\n");
        gpioDelay(inputRunTime);
        offMotors();
    }
        
    void turnRight(int inputTurnTime)
    {
        gpioWrite(leftFront_Forward, 1);
        gpioWrite(leftBack_Forward, 1);
        gpioWrite(rightFront_Backward, 1);
        gpioWrite(rightBack_Backward, 1);
        
        printf("Turning Right\n");
        gpioDelay(inputTurnTime);
        offMotors();
    }

    void turnLeft(int inputTurnTime)
    {
        gpioWrite(rightFront_Forward, 1);
        gpioWrite(rightBack_Forward, 1);
        gpioWrite(leftFront_Backward, 1);
        gpioWrite(leftBack_Backward, 1);
        
        printf("Turning Left\n");
        gpioDelay(inputTurnTime);
        offMotors();
    }

    void moveRight (int inputTurnTime)
    {
        gpioWrite(rightBack_Forward, 1);
        gpioWrite(leftFront_Forward, 1);
        gpioWrite(rightFront_Backward, 1);
        gpioWrite(leftBack_Backward, 1);
        
        printf("Moving Right\n");
        gpioDelay(inputTurnTime);
        offMotors();
    }

    void moveLeft(int inputTurnTime)
    {
        gpioWrite(rightFront_Forward, 1);
        gpioWrite(leftBack_Forward, 1);
        gpioWrite(rightBack_Backward, 1);
        gpioWrite(leftFront_Backward, 1);
        
        printf("Moving Left\n");
        gpioDelay(inputTurnTime);
        offMotors();
    }

    void wait(int inputWaitTime)
    {
        printf("Waiting\n");
        gpioDelay(inputWaitTime);
    }
}