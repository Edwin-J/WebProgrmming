#include <iostream>
#include <string>

using namespace std;

int main()
{

	char str1[20];
	char str2[20];


	cout << "str1�� ���ڿ��� �Է��ϼ��� : ";
	cin >> str1;
	cout << "str2�� ���ڿ��� �Է��ϼ��� : ";
	cin >> str2;

	int result = strcmp(str1, str2);

	if (result == 0)
		cout << "���� ���ڿ�" << endl;
	else if (result < 0)
		cout << "str1�� str2���� ���������� �տ� ����" << endl;
	else 
		cout << "str1�� str2���� ���������� �ڿ� ����" << endl;

}