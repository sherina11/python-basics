numbers = [3, 7, 2, 9, 5]

min_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num

print("Minimum number is:", min_num)