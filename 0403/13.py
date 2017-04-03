sum = 0;

while True :
    num = float(input("숫자를 입력하시오 : "));
    sum += num;

    boo = input("계속 ? (yes/no) : ");
    if boo == "yes" :
        continue;

    else :
        print("합 : ", sum);
        break;

        
