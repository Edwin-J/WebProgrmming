import math;

x1 = int(input("x1 좌표를 입력하세요 : "));
y1 = int(input("y1 좌표를 입력하세요 : "));
x2 = int(input("x2 좌표를 입력하세요 : "));
y2 = int(input("y2 좌표를 입력하세요 : "));



dis = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print(dis);
