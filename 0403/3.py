height = float(input("신장을 입력하세요 : "));
weight = float(input("체중을 입력하세요 : "));

bmi = weight / ((height/100) * (height/100));

print("BMI = ", bmi);
