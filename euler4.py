#4
def is_palindrome(number):
    return str(number) == str(number)[::-1]

def largest_palindrome():
    largest = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if is_palindrome(product) and product > largest:
                largest = product
        
    return largest

print(largest_palindrome())