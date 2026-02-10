num = 20
num = num //3 #taban bölme
print("num:",num)

num1 = 2
num1 = num1 ** 5
#num1 **= num1
print("num1:",num1)

print('Hello World'[-2])
print('Hello'*2)
print('Sample String'[:3])
print('Sample String'[1:6:2])

string = 'Hello'
string1 = ' '
string2 = 'World'
print(string, string1, string2) #virgül otomatik boşluk atar
print(string,string1,string2, sep ='' )
print(string,string1,string2, sep ='***' )
 
exString = """
Python's name does not come from a 
'snake'
"""
print(exString)

sampleBinary = 0B1010
print(sampleBinary)
print(type(sampleBinary))
sampleOctave = 0o543
print(sampleOctave)
print(type(sampleOctave))
sampleHexadecimal = 0X2F3
print(sampleHexadecimal)
print(type(sampleHexadecimal)) 
sampleBigFloat = 1.8E23 # 1.8 x 10^23
print(sampleBigFloat)
print(type(sampleBigFloat))
sampleSmallFloat = 2.3E-54
print(sampleSmallFloat)
print(type(sampleSmallFloat))

string3 = "This is \"stupid\" example for printing"
string3 += ' \'\x61\', \'\xAE\' and \'\uA7B5\' characters '
string3 += "\t because it is for presenting escape sequence" 
print(string3)

firstName = "meryem"
lastName = "karabakal"
formattedMessage = f"{firstName:10} [{lastName:10}] is a poet"
print(formattedMessage)
formattedMessage = f"{firstName:.2} [{lastName:.3}] is a poet"
print(formattedMessage)
formattedMessage = f"{firstName:10.2} [{lastName:10.2}] is a poet"
print(formattedMessage)

number1 = 3
number2 = 6
print(f'{number1} plus {number2} is {number1+number2} and is not \
{2 * (number1 + number2)}')
piNumber = 3.1415936535
print(f"{{Pi Number}} is {{ {piNumber} }} and its half is {piNumber/2:.6}")
errorNO =12345
print(f"There is a {errorNO:b} error!")
print(f"There is a {errorNO:#b} error!")
print(f"There is a {errorNO:o} error!")
print(f"There is a {errorNO:#o} error!")
print(f"There is a {errorNO:X} error!")
print(f"There is a {errorNO:#X} error!")
print(f"There is a {errorNO:10X} error!")

number3 = 123123123123123123
print(f"{number3:,}")

message = "This is an example"
print(f"{message:<30}") #sola yaslar 30 a tamamlayacak kadar boşluk koyar
print(f"{message:>30}") #sağa yaslar
print(f"{message:^30}") #ortalar
print(f"{message:*>30}")
print(f"{message:?<30}")
print(f"{message:-^30}")

string4 = 'Python is gEneral purposE Programming languange'
print(string4.title())
print(string4.find('O'))
print(string4.find('p')) #sondan aramaya başlar
print(string4.replace('gEneral purposE','hight level'))
print('P' in string4) 

string5 = "Meryem"
print(id(string5))
string6 = "Meryem"
print(id(string6))
