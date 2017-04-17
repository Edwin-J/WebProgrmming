cnt = 0
tot = 0
while True:
    num1 = input('Enter a number:')
    
    if num1 == 'done':
        break;
    
    try:
        num2 = int(num1)
        
    except:
        print ('Error : Invalid input')
        continue;
    
    cnt += 1
    tot += num2
    
print ('Count = ', cnt,' Sum = ', tot, ' Ave = ', (tot / cnt))
