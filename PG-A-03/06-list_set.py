numbers = [3,7,9,2,4]
numbers1 = numbers.copy()
print("numbers:", numbers)
print("numbers id:", id(numbers))
print("numbers:", numbers)
print("numbers id:", id(numbers))

primeNumbers = {2,3,5,7,11,13,17,19}
primeNumbers.discard(7)
print(primeNumbers)
primeNumbers.pop()
print(primeNumbers)
primeNumbers.update({23,29},[31,37])
print(primeNumbers)
primeNumbers.clear()
print(primeNumbers)

evenNumbers = {number for number in range(2,51,2)}
print(evenNumbers)
multiplesOfThree = {number for number in range(3,50,3)}
print(multiplesOfThree)
print(evenNumbers | multiplesOfThree) #birleşim
print(evenNumbers.union(multiplesOfThree))
print(evenNumbers & multiplesOfThree) #kesişim
print(evenNumbers.intersection(multiplesOfThree))
print(evenNumbers - multiplesOfThree) #fark
print(evenNumbers.difference(multiplesOfThree))
print(evenNumbers ^ multiplesOfThree) #simetrik fark
print(evenNumbers.symmetric_difference(multiplesOfThree))



