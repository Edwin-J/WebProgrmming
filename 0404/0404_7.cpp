#include<iostream>
#include<string>
using namespace std;

class Car{
private:
	int speed;
	int gear;
	string color;

public:
	Car(){
		cout << "����Ʈ ������ ȣ��" << endl;
		speed = 0;
		gear = 1;
		color = "white";
	}
};

int main(){
	Car c1;
	return 0;
}