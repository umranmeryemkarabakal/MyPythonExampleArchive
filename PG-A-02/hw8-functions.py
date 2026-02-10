def prime_number(num1, num2):

    for num in range(num1, num2+1):
        if num>1:
            for i in range(2, num):
                if num%i == 0:
                    break
            else:
                print(num)

prime_number(4,8)

def full_parts(num):
    full_parts_list = [1]
    for i in range(2, num):
        if num%i ==0:
            full_parts_list.append(i)
    full_parts_list.append(num)
    return full_parts_list

print(full_parts(12))