# ZeroDivisionError
print('Give me two number, and I will divide them.')
print('Enter "q" to exit.\n')
while True:
    first_number = input('First number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print('You cannot divide by zero!')
    else:
        print(answer)