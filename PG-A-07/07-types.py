
def zip_example():
    a = [1, 2, 3]
    b = ["a", "b", "c"]
    return zip(a, b)  # `zip` objesi döner
result = zip_example()
print(type(result))  # <class 'zip'>
# Eğer listeye çevirirsek:
print(list(result))  # [(1, 'a'), (2, 'b'), (3, 'c')]



def args_example(*args):
    return args  # Tuple döner
result = args_example(1, 2, 3, "a", "b")
print(type(result))  # <class 'tuple'>
print(result)  # (1, 2, 3, 'a', 'b')



def kwargs_example(**kwargs):
    return kwargs  # Dict döner
result = kwargs_example(name="Alice", age=25)
print(type(result))  # <class 'dict'>
print(result)  # {'name': 'Alice', 'age': 25}



def zip_args(*args):
    return list(zip(*args))  # Liste döndürülür
result = zip_args([1, 2, 3], ["a", "b", "c"])
print(result)  # [(1, 'a'), (2, 'b'), (3, 'c')]



def zip_kwargs(**kwargs):
    return list(zip(kwargs.keys(), kwargs.values()))  # Dict elemanlarını tuple yapar
result = zip_kwargs(a=1, b=2, c=3)
print(result)  # [('a', 1), ('b', 2), ('c', 3)]



def return_none():
    return  # None döner

result = return_none()
print(type(result))  # <class 'NoneType'>
