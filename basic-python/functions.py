#  create a function
def myPet(pet_name = 'dog'):
    print("i have a pet "+ pet_name)
myPet('cat')

# write a function to return a value
def getProduct(num1, num2):
    return num1*num2
product = getProduct(5,8)
print('Product is ', product)

# scope of variable with number
def addOnetoNum(num):
    num += 1
    print('Number inside the function :', num)

    return
num = 4
addOnetoNum(num)
print('Number Outside the function :', num)

# scope of variable of type list
def addOnetoList(list):
    list.append(4)
    print('List inside the function :', list)
    return

myList = [ 2, 4, 5, 6]
addOnetoList(myList)
print('List Outside the function :', myList)
