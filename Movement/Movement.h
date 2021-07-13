#pragma once

#include <stdio.h>
#include <pigpio.h>

namespace Movement
{
    static int runTime = 2000;
    static int waitTime = 1000;
    static int turnTime = 500;

    static void setup();
    static void cleanup();

    static void offMotors();
    static void wait(int inputWaitTime);

    static void movementTest();
    static void PWMtest();

    static void moveForward(int inputRunTime);
    static void moveBackward(int inputRunTime);
    static void moveRight (int inputTurnTime);
    static void moveLeft(int inputTurnTime);
        
    static void turnRight(int inputTurnTime);
    static void turnLeft(int inputTurnTime);
};