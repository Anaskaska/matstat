import numpy as np

def sum_numbers(numbers):
    summa = 0
    for number in numbers:
        summa += number
    return summa

z = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
x = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
y = []
n = len(x)
avr = sum_numbers(x) / n
print(f"Мат ожидание ", avr, np.mean(z))
for index, elem in enumerate(x):
    y[index] = (elem - avr)**2
print(y)
d1 = sum_numbers(y) / n
d2 = sum_numbers(y) / n - 1

print(f"Смещенная оценка дисперсии ", d1, "  ", np.var(z))
print(f"Несмещенная оценка дисперсии ", d2, "  ", np.var(z, ddof=1))




