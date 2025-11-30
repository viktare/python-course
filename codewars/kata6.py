def is_prime(num):
    if num <= 1:
        return False

    numbers = range(2, num)
    for number in numbers:
        prime: float = num / number
        if prime.is_integer():
            return False
        else:
            continue
        
    return True 

# print(is_prime(3))

def is_prime_correct(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for number in range(3, num, 2):
        if num % number == 0:
            return False

    return True

print(is_prime_correct(2**31))