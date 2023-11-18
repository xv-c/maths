import numpy as np
import pandas as pd
from sympy import symbols, Eq, Matrix, solve
from scipy.optimize import minimize

file_names = [
    'files/sb.csv',
    'files/hy.csv',
    'files/nv.csv',
    'files/mv.csv'
]

all_daily_returns = []
for file_name in file_names:
    # Чтение CSV файла
    df = pd.read_csv(file_name)

    # Преобразование столбца 'CLOSE' в массив
    close_array = df['<CLOSE>'].values

    daily_returns = []
    for i in range(1, len(close_array)):
        previous_close = close_array[i - 1]
        current_close = close_array[i]
        daily_return = (current_close - previous_close) / previous_close
        daily_returns.append(daily_return)

    all_daily_returns.append(daily_returns)

expected_returns = []
for daily_returns in all_daily_returns:
    expected_return = np.mean(daily_returns)
    expected_returns.append(expected_return)

# Вывод ожидаемых доходностей
print("all")
for exp_return in expected_returns:
    print("\t", exp_return * 100, "%")

i1 = 1
i2 = 3


# Построение матрицы ковариации
covariance_matrix = [
    [np.cov(all_daily_returns[i1], all_daily_returns[i1]), np.cov(all_daily_returns[i1], all_daily_returns[i2])],
    [np.cov(all_daily_returns[i2], all_daily_returns[i1]), np.cov(all_daily_returns[i2], all_daily_returns[i2])]
]


ss = 0