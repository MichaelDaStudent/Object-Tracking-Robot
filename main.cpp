#include "Movement/Movement.h"

int main()
{
    Movement::setup();
    // Movement::motorTest();
    // Movement::PWMtest();
    Movement::movementTest();

    Movement::cleanup();
}