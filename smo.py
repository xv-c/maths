import random

# Количество серий экспериментов
m = 23
# Число членов выборки в каждой серии
n = 10000

# Максимальное значение для a
max_a = 10
# Максимальное значение для b
max_b = 5

avg_gs = []  # Список для хранения средних значений величины g
avg_hs = []  # Список для хранения средних значений величины h

std_gs = []  # Список для хранения стандартных отклонений величины g
std_hs = []  # Список для хранения стандартных отклонений величины h

# Цикл по сериям экспериментов
for idx in range(1, m + 1):
    n = n

    gs = []  # Список для хранения значений величины g
    hs = []  # Список для хранения значений величины h

    g_rasp = []  # Список для распределения g
    h_rasp = []  # Список для распределения h

    # Инициализация переменных для расчетов
    cum_a = 0
    cum_e = max_b * random.random()

    g_sum = 0  # Сумма значений g
    h_sum = 0  # Сумма значений h

    gs.append(0)
    hs.append(0)

    # Инициализация списков для распределений
    for k in range(11):
        g_rasp.append(0)
        h_rasp.append(0)

    # Цикл для вычисления значений g и h
    for i in range(1, n):
        a = max_a * random.random()
        b = max_b * random.random()
        c = cum_a + a
        d = max(c, cum_e)
        e = d + b
        f = e - c
        gs.append(f - b)
        hs.append(d - cum_e)
        cum_a = c
        cum_e = e

        # Обновление функций распределения для g и h
        if gs[i] <= 1:
            g_rasp[1] += 1

        if hs[i] <= 0:
            h_rasp[1] += 1

        for k in range(1, 11):
            if k - 1 < gs[i] <= k:
                g_rasp[k] += 1
            if k - 1 < hs[i] <= k:
                h_rasp[k] += 1

        if gs[i] > 10:
            g_rasp[10] += 1

        if hs[i] > 10:
            h_rasp[10] += 1

        g_sum += gs[i]  # Накопление суммы g
        h_sum += hs[i]  # Накопление суммы h

    # Нормировка распределений g и h
    for i in range(11):
        g_rasp[i] = g_rasp[i] / n
        h_rasp[i] = h_rasp[i] / n

    # Расчет средних значений g и h
    avg_g = g_sum / n
    avg_h = h_sum / n
    avg_gs.append(avg_g)
    avg_hs.append(avg_h)

    # Расчет дисперсий для g и h
    disp_g = sum([(gi - avg_g) ** 2 for gi in gs]) / n
    disp_h = sum([(hi - avg_h) ** 2 for hi in hs]) / n

    # Расчет стандартных отклонений для g и h
    std_g = disp_g ** 0.5
    std_h = disp_h ** 0.5
    std_gs.append(std_g)
    std_hs.append(std_h)

    # Вывод результатов для каждой серии
    print(f"\nN = {idx}")
    print(f"Распределение g: {g_rasp}")
    print(f"Распределение h: {h_rasp}")
    print(f"Среднее g: {avg_g}")
    print(f"Среднее h: {avg_h}")
    print(f"Средне-квадратичное отклонение g: {std_g}")
    print(f"Средне-квадратичное отклонение h: {std_h}\n")

t = 2.58

# Для величины g
epsilon_g = t * std_gs[0] / n ** 0.5
min_conf_g = avg_gs[0] - epsilon_g  # Нижняя граница доверительного интервала для g
max_conf_g = avg_gs[0] + epsilon_g  # Верхняя граница доверительного интервала для g
print(f"{min_conf_g} < mg < {max_conf_g}")

# Проверка, попадают ли средние значения g в доверительный интервал
for s in avg_gs:
    if not (min_conf_g < s < max_conf_g):
        print(f"s1 = {s} не попадает в доверительный интервал!")

# Для величины h
epsilon_h = t * std_hs[0] / n ** 0.5
min_conf_h = avg_hs[0] - epsilon_h  # Нижняя граница доверительного интервала для h
max_conf_h = avg_hs[0] + epsilon_h  # Верхняя граница доверительного интервала для h
print(f"{min_conf_h} < mh < {max_conf_h}")

# Проверка, попадают ли средние значения h в доверительный интервал
for s in avg_hs:
    if not (min_conf_h < s < max_conf_h):
        print(f"s2 = {s} не попадает в доверительный интервал!")