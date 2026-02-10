from random import choice, randint

characters = "sgj904*94ğoqpkalsdfnvkçxk*0380*ü2i3.wköş"

password = ""

for index in range(randint(8,16)):
    password += choice(characters) 

print(password)

