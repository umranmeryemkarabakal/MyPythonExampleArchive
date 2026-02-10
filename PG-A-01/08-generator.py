# generators
# bellekte yer kullanmayan iterator tanımlatır

def cube():
    for i in range(5):
        yield i ** 3

for i in cube():
    print(i)

generator = (i**3 for i in range(5)) # <generator object <genexpr> at 0x00000217D3AE62D0>
print(generator)

for i in generator:
    print(i)
    
# print(next(generator))
# print(next(generator))
# print(next(generator))
