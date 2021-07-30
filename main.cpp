#include "Movement/Movement.h"

int main()
{
    Movement::setup();

    Movement::movementTest();
    Movement::PWMtest();

    Movement::cleanup();
}