import math 

x = 2.8
print(round(x)) #yuvarlar
x = -3.9
print(abs(x)) 
x = 3.9
print(abs(x)) 

print(math.ceil(2.9)) #en yakın büyük tam sayıyı döndürür
print(math.ceil(-2.9))
print(math.floor(2.9)) #en yakın küçük sayıya yuvarlar
print(math.floor(-2.9)) #int sonuç verir
print(-2.9//1) #float sonuç verir

print(math.factorial(5))

radius = 3
print(f"circumference of a circle with radius {radius}: {radius * 2 * math.pi}")
print(f"circumference of a circle with radius {radius}: {radius * math.tau}")

print(3 ** 2)
print(math.pow(3,2)) #float döner
