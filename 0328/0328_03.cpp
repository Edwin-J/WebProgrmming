#include <iostream>
#include <string>

using namespace std;

int main()
{
	char str1[20];
	char str2[20];
	char str3[20];

	cout << "str1 ���ڿ��� �Է��ϼ��� : ";
	cin >> str1;

	strcpy(str2, str1); // ���ڿ��� �����ϴ� �Լ�
	strcpy(str3, "�����Ұž�");

	cout << "str2 = " << str2 << endl;
	cout << "str3 = " << str3 << endl;
}