#include<iostream>
#include<string>
using namespace std;

class Car {
private:
	int speed;
	int gear;
	string color;

public:
	Car(){
		cout << "������ ȣ��" << endl;
		speed = 0;
		gear = 1;
		color = "white";
	}
	~Car(){
		cout << "�Ҹ��� ȣ��" << endl;
	}
};

int main(){
	Car c1;
	return 0;
}