import math

def circle(r) :
    area = math.pi * r * r
    circle = 2 * math.pi * r
    return (area, circle)

r = float(input("원의 반지름을 입력하세요 : "))
(a, c) = circle(r)
print("넓이 : ", a , ", 원주 : ", c)
