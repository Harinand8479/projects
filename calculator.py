def add(n1, n2):
    result = n1 + n2
    print('Result is:', result)

def sub(n1, n2):
    result = n1 - n2
    print('Result is:', result)

def division(n1, n2):
    result = n1 / n2
    print('Result is:', result)

def multiply(n1, n2):
    result = n1 * n2
    print('Result is:', result)

ch = 'yes'
while ch == 'yes':
    print('ENTER 1 TO ADD THE NUMBERS')
    print('ENTER 2 TO SUBTRACT THE NUMBERS')
    print('ENTER 3 TO DIVIDE THE NUMBERS')
    print('ENTER 4 TO MULTIPLY THE NUMBERS')

    choice = int(input('ENTER YOUR CHOICE: '))
    n1 = int(input('ENTER 1ST NUMBER: '))
    n2 = int(input('ENTER 2ND NUMBER: '))

    if choice == 1:
        add(n1, n2)
    elif choice == 2:
        sub(n1, n2)
    elif choice == 3:
        division(n1, n2)
    elif choice == 4:
        multiply(n1, n2)
    else:
        print('Wrong choice!')

    ch = input('Do you wish to continue? (yes/no): ')
