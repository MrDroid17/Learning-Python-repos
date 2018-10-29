# For loop
persons = ['Sobhit', 'Rohit', 'Aish', 'Alexa', 'Tommy']

for person in persons:
    print('My name is - ', person)

# with range --- length of person = len(persons)
for i in range(len(persons)):
    print(str(i+1), 'person is - ', persons[i])

for i in range(0, 6):
    print(str(i+1), ' position is', i)


# While loop
index = 0;
while index <= 10:
    print('Count: ', index)
    if index == 7:
        break
    index += 1