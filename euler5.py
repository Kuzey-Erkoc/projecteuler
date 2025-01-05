#5
def ebob(a, b):
    while b:
        a, b = b, a % b
    return a

def ekok(a, b):
    return abs(a * b) // ebob (a, b)

result = 1

for i in range(1, 21):
    result = ekok(result, i)

print(result)
