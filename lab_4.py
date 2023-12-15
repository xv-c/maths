import numpy as np
import pandas as pd
import os


def hopf_portf(cb, x):
    num_cb = len(cb)  # Количество акций
    weight_matrix = np.zeros((num_cb, num_cb))
    for i in range(num_cb):
        for j in range(num_cb):
            weight_matrix[i][j] = x[i] * x[j]
            weight_matrix[i][i] = 0

    state_vector = [1, 1, 0, 1]
    stable = False

    while not stable:
        new_state_vector = np.sign(np.dot(weight_matrix, state_vector))
        if np.array_equal(state_vector, new_state_vector):
            stable = True
        state_vector = new_state_vector
    weights = []
    for i in range(num_cb):
        weights.append(x[i]) if state_vector[i] == 1 else weights.append(0.0)
    weights_sum = sum(weights)
    weights = [weight / weights_sum for weight in weights]
    return weights


file = os.path.join('.', 'files', 'all.csv')
# Загрузка данных о доходностях ценных бумаг
data = pd.read_csv(file)
# Извлечение доходностей
akcii = data.values
akcii = pd.DataFrame(akcii)
# находим ежедневную доходность
doxodn = akcii / akcii.shift(1) - 1
dox_sr = doxodn.iloc[1:, :]
# среднее по доходностям
cb = ['hydr', 'mvideo', 'novatek', 'sber']
x = dox_sr.mean()
weights = hopf_portf(cb, x)

# Вычисление корреляции между бумагами
correlation_matrix = dox_sr.corr()

# Вычисление риска портфеля
portfolio_variance = np.dot(np.array(weights).T, np.dot(correlation_matrix, weights))
risks = dox_sr.std()
portfolio_risk = np.sqrt(portfolio_variance)

print("Веса:", weights)
print()

print("Риск каждой бумаги:")
for i in range(len(cb)):
    print(cb[i], risks[i])
print()

print("Риск портфеля:", portfolio_risk)
print()

print("Доходность портфеля:", np.dot(np.array(weights), x))
print()

optimized_weights = np.round(weights, 2)
print(optimized_weights)
print(sum(optimized_weights))
