inNum = int(input("수를 입력하세요 : "));

num = range(1, inNum + 1);

sum = 1;
i = 1;

for i in num :
    sum = sum * i;

print("팩토리얼의 합 : ", sum);
