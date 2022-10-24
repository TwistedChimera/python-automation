def collatz(number):
        if(int(number) % 2 == 0):
           print(int(number) // 2, end=' ')
           return int(number) // 2
        else:
            print(3 * int(number) + 1, end=' ')
            return 3 * int(number) + 1

       
print('enter a number: ', end='')
start=input()
try:
    
    print(int(start), end=' ')
    while True:
        start=collatz(int(start))
        if(int(start) == 1):
            break
            
except ValueError:
    print('You must enter an integer.')
        


