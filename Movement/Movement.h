#pragma once

#include <iostream>
#include <stdio.h>
#include <pigpio.h>

namespace Movement
{
    extern float runTime;
    extern float waitTime;
    extern float turnTime;

    void setup();
    void cleanup();

    void offMotors();
    void wait(int inputWaitTime);

    void motorTest();
    void movementTest();
    void PWMtest();

    void moveForward(int inputRunTime);
    void moveBackward(int inputRunTime);
    void moveRight (int inputTurnTime);
    void moveLeft(int inputTurnTime);
        
    void turnRight(int inputTurnTime);
    void turnLeft(int inputTurnTime);
};