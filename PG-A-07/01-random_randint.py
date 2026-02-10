from random import randint

my_string = "meryem"
my_list = [eleman for eleman in my_string]
print(my_list)
 
print(type(randint(0,20)))
my_num_1 = randint(0,20) # rastgele değer verir 0 ve 20 dahil

print(type(range(0,20)))
my_range_list = list(range(0,20)) # 0dan 20e elemanları dizer, 20 dahil değildir
print(my_range_list)

my_enumarete_list = list(enumerate(my_range_list))
print(my_enumarete_list)

# key value pairing : anahtar kelime değer eşleşmesi

