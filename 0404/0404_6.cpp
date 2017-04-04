#include<iostream>
#include<string>
using namespace std;

class Car {
public:
	int getSpeed();
	void setSpeed(int s);
	void honk();

private:
	int speed;
};

int Car::getSpeed(){
	return speed;
}

void Car::setSpeed(int s){
	speed = s;
}

void Car::honk(){
	cout << "빠아아아아아아아아앙ㅇ~~" << endl;
}

int main(){
	Car myCar;

	myCar.setSpeed(80);
	myCar.honk();
	cout << "현재 속도는 " << myCar.getSpeed() << endl;

	return 0;

}