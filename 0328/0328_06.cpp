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

	strcat(str1, str2); // �ڿ��� �̾��ִ� �Լ�

	cout << "str : " << str1 << endl;

}