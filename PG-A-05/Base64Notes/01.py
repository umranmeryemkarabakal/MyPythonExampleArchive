import base64

string = "python is awesome"
stringAsBytes = string.encode('utf-8')
stringAsBase64 = base64.b64encode(stringAsBytes)
print(stringAsBase64)

string = stringAsBase64.decode('utf-8')
print(string)

stringAsBase64_1 = b'cHl0aG9uIGlzIGF3ZXNvbWU='
stringAsBinary = base64.b64decode(stringAsBase64_1)
print(stringAsBinary)

string1 = stringAsBinary.decode('utf-8')
print(string1)


from math import log,ceil

number = 1376892233448
print("bit form of number:",bin(number))

numberOffByte = ceil(log(number, 2) / 8) #2 tabanında logaritması alınarak .... log string döndürür ceil yuvarlama yapparak çalışır


numberAsBytes = number.to_bytes(numberOffByte, byteorder= 'little') #sayı kaç bytese o girilir fazla grilirse kalan yerleri sıfır ile doldurur
#byteorder : hafızada bytların nasıl sıralandığıdır
print("bytes of the number: ", numberAsBytes)

numberAsBase64 = base64.b64encode(numberAsBytes)
print("base64 form of number: ", numberAsBase64)


numberAsBase64_1 = b'\xe8&,\x95@\x01'

numberAsBytes_1 = base64.b64decode(numberAsBase64_1)
print("bytes of the number: ", numberAsBytes_1)

number1 = int.from_bytes(numberAsBytes_1,byteorder='little')
print(number1)
