#This session is used for a simple calculator
print('Here are some option that can be used according to the user interest \n (1)addition \n (2) subtration \n (3)division \n (4)multipliation \n (5)square ')
a = int(input("Enter the required option number? "))
if a==1:
    b=input('Enter the first number to be added...')
    c= input('Enter the second number to be added...')
    sum=int(b)+int(c)
    print('The sum of the given numbers are... ',sum)
elif a==2:
    b = input('Enter the first number to be  subtraction...')
    c = input('Enter the second number to be  subtraction...')
    sub = int(b) - int(c)
    print('The subtraction of the given numbers are... ', sub)
elif a==3:
    b = input('Enter the first number to be multiplied...')
    c = input('Enter the second number to be  multiplied...')
    mul = int(b) * int(c)
    print('The multiplication of the given numbers are... ', mul)
elif a==4:
    b = input('Enter the first number to be divided...')
    c = input('Enter the second number to be  divided...')
    div = int(b) * int(c)
    print('The division of the given numbers are... ', div)
elif a==5:
    b = input('Enter the first number to be squared...')
    sqr = int(b)*int(b)
    print('The square of the given number is... ', sqr)
elif a==6:
    b = input('Enter the first number to be divided...')
    c = input('Enter the second number to be  divided...')
    div = int(b) * int(c)
    print('The division of the given numbers are... ', div)