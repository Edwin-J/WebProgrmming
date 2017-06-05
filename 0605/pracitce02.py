fhand = open('words.txt')
li = []

for line in fhand :
    words = line.split()

    for word in words :
        if not word in li :
            li.append(word)

print("단어 수 : ", len(li))
