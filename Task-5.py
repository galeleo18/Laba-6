C = "С"
c = "с"
A = ["Санс", "Арбуз", "Доместос", "Слайс", "Салат"]

count = 0
for word in A:
    if len(word) > 1 and word.startswith(C) and word.endswith(c):
        count += 1

print("Количество подходящих элементов:", count)