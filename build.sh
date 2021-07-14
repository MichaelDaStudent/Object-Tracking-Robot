g++ -c ./main.cpp
g++ -c ./Movement/Movement.cpp
g++ -Wall -pthread -o ObjectTrackingRobot main.o Movement.o -lpigpio -lrt && ./ObjectTrackingRobot