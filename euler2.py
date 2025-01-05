#2
a, b = 1, 2
total_sum = 0

while b <= 4_000_000:
    if b % 2 == 0:  
        total_sum += b
    a, b = b, a + b 

print(total_sum)