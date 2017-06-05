list = ['-10.8', '0', '1', '18', '23.6', '45', '63', '86.1']

try :
    room = input("찾을 번호를 입력하세요 : ")
    print(room,"은 ", list.index(room),"번째 방에 있습니다.")

except :
    print("해당 번호가 리스트에 존재하지 않습니다.")
