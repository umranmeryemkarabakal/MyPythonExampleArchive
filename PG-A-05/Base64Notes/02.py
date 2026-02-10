import base64
from math import log, ceil

# Metni base64'e kodlama
string = "python is awesome"
stringAsBytes = string.encode('utf-8')
stringAsBase64 = base64.b64encode(stringAsBytes)
print(stringAsBase64)

# Base64 dizesini metne dönüştürme
decoded_string = base64.b64decode(stringAsBase64).decode('utf-8')
print(decoded_string)

# Hatalı bayt dizisini base64'den çözümlemek
numberAsBase64_1 = b'cHl0aG9uIGlzIGF3ZXNvbWU='
decoded_number = base64.b64decode(numberAsBase64_1)
print(decoded_number)

# İkinci hatalı bayt dizisini base64'den çözümlemek
numberAsBase64_2 = b'6CYslUAB'
decoded_number_2 = base64.b64decode(numberAsBase64_2)
print(decoded_number_2)

# Sayıyı base64'e kodlama
number = 1376892233448
print("bit form the number:", bin(number))

numberOffByte = ceil(log(number, 2) / 8)

numberAsBytes = number.to_bytes(numberOffByte, byteorder='little')
print("bytes of the number: ", numberAsBytes)

numberAsBase64 = base64.b64encode(numberAsBytes)
print("base64 from the number: ", numberAsBase64)

# Hatalı bayt dizisini base64'den çözümlemek
numberAsBase64_3 = b'e8&,\x95@\x01'
decoded_number_3 = base64.b64decode(numberAsBase64_3)
print(decoded_number_3)

# Bayt dizisini sayıya dönüştürme
number1 = int.from_bytes(decoded_number_3, byteorder='little')
print(number1)
