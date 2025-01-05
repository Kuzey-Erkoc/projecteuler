#1
total_sum = 0  

for number in range(100):  
    if number % 3 == 0 or number % 5 == 0:  
        total_sum += number  

print(total_sum)