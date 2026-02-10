def greetUser(firstName: str, lastName:str, message: str = "welcome"):
    print(f'Hi {firstName} {lastName}')
    if message is not None :
        print(message)

greetUser('Meryem','Karabakal')
print("---")
greetUser('Meryem','Karabakal',None)


numbers = [1,2,3,4,5,6,7,8,9,10]
squares = []
for number in numbers:
    squares.append(number**2)
squares1 = [number for number in numbers]
print(squares1)

names = ["james","Kirck","rosa","emily","Emma"]
namestartWithO = [ name for name in names if name.upper().startswith('e')]

list1 = [20,30,40]
list2 = [4,8,7,0]
newList = [ x*y for x in list1 for y in list2]
print(newList)

coordinates = [5,8,6,9,7,1]
for index in range(len(coordinates)//3):
    x,y,z = coordinates[index * 3 : 3 + index *3]
    print(x*y*z)

