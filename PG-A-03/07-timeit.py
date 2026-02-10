import sys
import timeit

evenNumberList = [number for number in range(2,1001,2)]
evenNumberTuple = tuple(evenNumberList)

print("list size:",sys.getsizeof(evenNumberList))
print("tuple size:",sys.getsizeof(evenNumberTuple))

print("List time test: ",timeit.timeit(stmt="numbers = [ 1,2,3,4,5,6,7,8,9]"))
print("List time test: ",timeit.timeit(stmt="numbers = ( 1,2,3,4,5,6,7,8,9)"))

del(evenNumberList[5])
del(evenNumberTuple)