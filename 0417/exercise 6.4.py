num = [0, 0, 0, 0, 0]
i = 0
ave = 0

for i in range(5) :
    num[i] = int(input("정수를 입력하세요 : "))
    ave = ave + num[i]
    i = i + 1

ave = ave / 5

i = 0

print("평균 : ", ave)
