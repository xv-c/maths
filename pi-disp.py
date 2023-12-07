import random
import numpy as np

def calculate_circle_area(N):
    r = 5
    m = 0
    for _ in range(N):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if x**2 + y**2 <= r**2:
            m += 1
    return (2 * r)**2 * (m / N)

# Формирование таблицы с результатами экспериментов, средним и дисперсией
results = []
Ns = [100, 200, 500, 1000, 2000, 5000, 10000]
for N in Ns:
    areas = [calculate_circle_area(N) for _ in range(10)]  # 10 экспериментов для каждого N
    mean_area = np.mean(areas)
    variance_area = np.var(areas)
    results.append((N, areas, mean_area, variance_area))

# Вывод результатов
print("N\t\tВычисленные площади\t\t\t\t\t\t\t\t\t\t\tСреднее\t\tДисперсия")
for result in results:
    N, areas, mean_area, variance_area = result
    # Форматирование площадей с двумя знаками после запятой
    areas_formatted = [f"{area:.2f}" for area in areas]
    print(f"{N}\t\t{areas_formatted}\t\t{mean_area:.2f}\t\t{variance_area:.2f}")