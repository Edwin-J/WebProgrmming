#define STUDENTS 5

#include <iostream>
using namespace std;

int main()
{
	int grade[STUDENTS];
	int sum = 0;
	int i, average;
	for (i = 0; i < STUDENTS; i++){
		cout << "�л����� ������ �Է��Ͻÿ� : ";
		cin >> grade[i];
	}
	for (i = 0; i < STUDENTS; i++)
		sum += grade[i];

	average = sum / STUDENTS;
	cout << "���� ��� = " << average << endl;

}