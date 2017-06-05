fhand = open('mbox-short.txt')
cnt1 = 0
cnt2 = 0

fname = input("찾을 사람의 이름을 입력해 주세요 : ")

for line in fhand :
    line = line.rstrip()
    if line.startswith('From: ') :
        line = line[6:]
        index = line.find('@')
        line = line[:index]
        cnt1 += 1
        
            
    if fname == line :
        cnt2 += 1

print(fname, "이 보낸 횟수 : ", cnt2)
