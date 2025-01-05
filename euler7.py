#7

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_nth_prime(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
        num += 1
    return num - 1

print(find_nth_prime(10001)) 