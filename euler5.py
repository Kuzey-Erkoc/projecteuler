#5
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd (a, b)

result = 1

for i in range(1, 21):
    result = lcm(result, i)

print(result)