from time import sleep
print('Welcome to the CALCULATOR')
sleep(2)
num1 = float(input('Enter a number: '))
num2= float(input('Enter another number:'))
operator = input('Choose an operator (+, -, *, /): ')
if operator == '+':
    result = num1+num2
    print('The result is:', result)

elif operator == '-':
    result=  num1-num2
    print('The result is: ', result)

elif operator == '*':
    result = num1*num2
    print('The result is: ', result)

elif operator == '/':
    result = num1/num2
    print('The result is: ', result)

else:
    print('invalid operation')
    
    