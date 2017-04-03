num = int(input("정수 입력 : "));

sum = 0;
cnt = num;

while True :
    if cnt == 0 :
        break;
    
    sum += cnt % 10;
    cnt //= 10;

print("각 자릿수의 합 : ", sum)
