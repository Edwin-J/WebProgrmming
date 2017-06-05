fhand = open('romeo.txt')
li = []

for line in fhand :
    
    words = line.split()

    for word in words :
        if not word in li :
            li.append(word)

li.sort()
print(li)
    
