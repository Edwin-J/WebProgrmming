money = int(input("투입한 돈 : "));
cost = int(input("물건 값 : "));

rem = money - cost;

print("거스름돈 : ", rem);

five = int((rem / 100) / 5);

print("500원 동전의 갯수 : ", five);

one = int((rem / 100) % 5);

print("100원 동전의 갯수 : ", one);
