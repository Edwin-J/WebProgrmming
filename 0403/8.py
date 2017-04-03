import random

num1 = random.randint(1, 100);
num2 = random.randint(1, 100);

if num1 < num2 :
    cnt = num1;
    num1 = num2;
    num2 = cnt;

asw1 = int(num1 - num2);

print(num1, "-", num2, "= ?");
asw2 = int(input());

if (asw1 == asw2) :
    print("정답입니다 ! ");

else :
    print("오답입니다.");
