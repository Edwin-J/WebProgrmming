import random;

while True :
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    sum = num1 + num2;
    print (num1, "+", num2, "= ? ");
    asw = int(input());

    if sum == asw :
        print ("잘했어요 !")

    else :
        print ("다음에는 잘할 수 있죠 ?")
        break
