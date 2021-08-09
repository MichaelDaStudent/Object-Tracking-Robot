#include "Movement.h"
#define SECONDS_TO_MICRO * 1000000

namespace Movement
{
    int runTime = 2 SECONDS_TO_MICRO;
    int waitTime = 1 SECONDS_TO_MICRO;
    int turnTime = 0.5 SECONDS_TO_MICRO;
    
    const int RIGHT_FRONT_FORWARD = 26;
    const int RIGHT_BACK_FORWARD = 5;
    const int LEFT_FRONT_FORWARD = 16;
    const int LEFT_BACK_FORWARD = 12;
    
    const int RIGHT_FRONT_BACKWARD = 20;
    const int RIGHT_BACK_BACKWARD = 13;
    const int LEFT_FRONT_BACKWARD = 19;
    const int LEFT_BACK_BACKWARD = 6;
    
    const int ENABLE = 25;

    void setup()
    {
        gpioInitialise();

        gpioSetMode(RIGHT_FRONT_FORWARD, PI_OUTPUT);
        gpioSetMode(RIGHT_BACK_FORWARD, PI_OUTPUT);
        gpioSetMode(LEFT_FRONT_FORWARD, PI_OUTPUT);
        gpioSetMode(LEFT_BACK_FORWARD, PI_OUTPUT);

        gpioSetMode(RIGHT_FRONT_BACKWARD, PI_OUTPUT);
        gpioSetMode(RIGHT_BACK_BACKWARD, PI_OUTPUT);
        gpioSetMode(LEFT_FRONT_BACKWARD, PI_OUTPUT);
        gpioSetMode(LEFT_BACK_BACKWARD, PI_OUTPUT);
        gpioSetMode(ENABLE, PI_OUTPUT);

        offMotors();
        gpioSetPWMrange(ENABLE, 100);
        gpioPWM(ENABLE, 100);
    }

    void cleanup()
    {
        gpioTerminate();
    }

    void offMotors()
    {
        gpioWrite(RIGHT_FRONT_FORWARD, 0);
        gpioWrite(RIGHT_BACK_FORWARD, 0);
        gpioWrite(LEFT_FRONT_FORWARD, 0);
        gpioWrite(LEFT_BACK_FORWARD, 0);

        gpioWrite(RIGHT_FRONT_BACKWARD, 0);
        gpioWrite(RIGHT_BACK_BACKWARD, 0);
        gpioWrite(LEFT_FRONT_BACKWARD, 0);
        gpioWrite(LEFT_BACK_BACKWARD, 0);
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
        gpioPWM(ENABLE, 0);

        for(int i = 1; i <= 100; i ++)
        {
            gpioPWM(ENABLE, i);
            moveForward(0.1 SECONDS_TO_MICRO);
        }
    }

    void moveForward(int inputRunTime)
    {
        gpioWrite(RIGHT_FRONT_FORWARD, 1);
        gpioWrite(LEFT_FRONT_FORWARD, 1);
        gpioWrite(LEFT_BACK_FORWARD, 1);
        gpioWrite(RIGHT_BACK_FORWARD, 1);

        printf("Moving Forward\n");
        gpioDelay(inputRunTime);
        offMotors();
    }

    void moveBackward(int inputRunTime)
    {
        gpioWrite(RIGHT_FRONT_BACKWARD, 1);
        gpioWrite(LEFT_FRONT_BACKWARD, 1);
        gpioWrite(RIGHT_BACK_BACKWARD, 1);
        gpioWrite(LEFT_BACK_BACKWARD, 1);
        
        printf("Moving Backward\n");
        gpioDelay(inputRunTime);
        offMotors();
    }
        
    void turnRight(int inputTurnTime)
    {
        gpioWrite(LEFT_FRONT_FORWARD, 1);
        gpioWrite(LEFT_BACK_FORWARD, 1);
        gpioWrite(RIGHT_FRONT_BACKWARD, 1);
        gpioWrite(RIGHT_BACK_BACKWARD, 1);
        
        printf("Turning Right\n");
        gpioDelay(inputTurnTime);
        offMotors();
    }

    // void improvedTurn(float inputAngle, float inputDistance, int inputTurnTime)
    // {
    //     std::string direction = "";
    //     float anglePercent = (inputAngle / 360) * 100;
    //     float distancePercent = inputDistance * 100;

    //     if(anglePercent == 0)
    //     {

    //     }
    // }

    // void improvedTurn(float inputAngle, float inputDistance)
    // {
    //     improvedTurn(inputAngle, inputDistance, 3 SECONDS_TO_MICRO);
    // }





    void turnLeft(int inputTurnTime)
    {
        gpioWrite(RIGHT_FRONT_FORWARD, 1);
        gpioWrite(RIGHT_BACK_FORWARD, 1);
        gpioWrite(LEFT_FRONT_BACKWARD, 1);
        gpioWrite(LEFT_BACK_BACKWARD, 1);
        
        printf("Turning Left\n");
        gpioDelay(inputTurnTime);
        offMotors();
    }

    void moveRight(int inputTurnTime)
    {
        gpioWrite(RIGHT_BACK_FORWARD, 1);
        gpioWrite(LEFT_FRONT_FORWARD, 1);
        gpioWrite(RIGHT_FRONT_BACKWARD, 1);
        gpioWrite(LEFT_BACK_BACKWARD, 1);
        
        printf("Moving Right\n");
        gpioDelay(inputTurnTime);
        offMotors();
    }

    void moveLeft(int inputTurnTime)
    {
        gpioWrite(RIGHT_FRONT_FORWARD, 1);
        gpioWrite(LEFT_BACK_FORWARD, 1);
        gpioWrite(RIGHT_BACK_BACKWARD, 1);
        gpioWrite(LEFT_FRONT_BACKWARD, 1);
        
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