fhand = open('students.txt')
li = []

for line in fhand :
    line = line.strip()
    print(line)
    words = line.split(",")
    for word in words :
        print("-", word)
