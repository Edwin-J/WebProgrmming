#include<iostream>
#include<string>
using namespace std;

class Rectangle{
	int width;
	int height;

public:
	int getWidth(){ return width; }
	void setWidth(int w){
		width = w;
	}

	int getHeight(){ return height; }
	void setHeight(int h){
		height = h;
	}

	int getArea(){ return width * height; }
};

int main(){
	Rectangle rect;
	rect.setWidth(3);
	rect.setHeight(5);
	cout << "�簢���� ������ " << rect.getArea() << endl;

	return 0;
}