#pragma once

#include <stdio.h>
#include <pigpio.h>

namespace Movement
{
    extern int runTime;
    extern int waitTime;
    extern int turnTime;

    void setup();
    void cleanup();

    void offMotors();
    void wait(int inputWaitTime);

    void movementTest();
    void PWMtest();

    void moveForward(int inputRunTime);
    void moveBackward(int inputRunTime);
    void moveRight (int inputTurnTime);
    void moveLeft(int inputTurnTime);
        
    void turnRight(int inputTurnTime);
    void turnLeft(int inputTurnTime);
};