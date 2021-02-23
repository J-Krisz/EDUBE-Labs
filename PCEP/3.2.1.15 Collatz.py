co = int(input('Enter a number: '))
steps = 0

while co != 1:
        if co % 2 == 0:
            co //= 2
            steps += 1
            print(co)
            if co == 1:
                print('steps = ' + str(steps))
        elif co % 2 == 1:
            co = 3 * co + 1
            steps += 1
            print(co)
            if co == 1:
                print('steps = ' + str(steps))
            
