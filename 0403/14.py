import random

num = random.randint(1, 100)
cnt = 1;

while True :
    inNum = int(input("숫자를 입력하시오 : "))

    if num == inNum :
        print("정답입니다!. 시도횟수 : ", cnt)

    elif num < inNum :
        print ("낮음")

    elif num > inNum :
        print ("높음")

    cnt += 1
