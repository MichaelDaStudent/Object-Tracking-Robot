#include "Movement/Movement.h"

int main()
{
    Movement::setup();

    Movement::movementTest();
    Movement::PWMtest();

    // while(true)
    // {
    //     moveRight(runTime);
    //     moveLeft(runTime);
    // }

    Movement::cleanup();
}