email = input("이메일 주소를 입력해 주세요 : ")
id = email.find('@')
print("아이디 : " + email[:id])
