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

    print(state_vector)

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
doxodn = (akcii / akcii.shift(1) - 1) * 100
dox_sr = doxodn.iloc[1:, :]
# среднее по доходностям
mean1 = dox_sr.mean()
cb = ['hydr', 'mvideo', 'novatek', 'sber']
x = mean1
weights = hopf_portf(cb, x)

print("Веса:", weights)
optimized_weights = np.round(weights, 2)
print(optimized_weights)
print(sum(optimized_weights))

n = len(akcii)

# Расчет риска и доходности портфеля
def calculate_portfolio_return_and_risk(weights, returns):
    portfolio_return = np.sum(returns.mean() * weights) * n
    portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * n, weights)))
    return portfolio_return, portfolio_std_dev

# Расчет доходности и риска для оптимизированных весов
portfolio_return, portfolio_risk = calculate_portfolio_return_and_risk(optimized_weights, dox_sr)

print("Ожидаемая доходность портфеля: ", portfolio_return)
print("Риск портфеля: ", portfolio_risk)
