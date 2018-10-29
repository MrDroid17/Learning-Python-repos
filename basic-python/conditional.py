x = 8

# if statement
if x > 6:
    print('x is greater than 6.')

# if-else
if x > 6:
    print('x is greater than 6.')
else:
    print('x is smaller than 6')

# if-elif-else
if x > 6:
    print('x is greater than 6.')
elif x < 6:
    print('x is smaller than 6')
else:
    print('x is equal to 6')

# nested if

# str = "you are in nested statement"
str = "4"
if x>6:
    if str.isnumeric():
        print('str is a number', str)
    else:
        print('str is a string', str)
