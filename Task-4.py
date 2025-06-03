numbers = [-3, -1, 2, 5, -7, 8, -2, 4]

first_positive = None
last_negative = None

for number in numbers:
    if first_positive is None and number > 0:
        first_positive = number
    if number < 0:
        last_negative = number

print("Первый положительный:", first_positive)
print("Последний отрицательный:", last_negative)