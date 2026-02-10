import math

for outerIndex in range(1,6):
    for innerIndex in range(1,6):
        print(f"{outerIndex*innerIndex:4}", end='')
    print()

print("\n\n")

for outerIndex in range(1,6):
    for innerIndex in range(1,6):
        if innerIndex == 3:
            continue
        print(f"{outerIndex*innerIndex:4}", end='')
    print()

print("\n\n")

for outerIndex in range(1,6):
    for innerIndex in range(1,6):
        if outerIndex == 3:
            continue
        print(f"{outerIndex*innerIndex:4}", end='')
    print()


def finfMaxDigit(number:int) -> int:
    remainder = number 
    numberOfDigits = math.floor(math.log10(number))
    maxDigit = 0
    while remainder >0:
        lefDigit = 