mkdir -p ./bin &&
g++ -c ./main.cpp -o bin/main.o &&
g++ -c ./Movement/Movement.cpp -o bin/Movement.o &&
g++ -Wall -pthread -o ObjectTrackingRobot bin/main.o bin/Movement.o -lpigpio -lrt &&
sudo killall pigpiod
sudo ./ObjectTrackingRobot