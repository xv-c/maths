import sympy as sp

# Определение матрицы
matrix = sp.Matrix([
    [-0.192307692, 0.230769231, 0],
    [0.230769231, -0.076923077, 0],
    [0.846153846, -1.615384615, 1],
])

# Определение переменных
x, y, z = sp.symbols('x y z')

# Определение вектора
vector = sp.Matrix([[x + 3900], [y + 4940], [z + 5120]])

# Умножение матрицы на вектор
result = matrix * vector

# Подстановка значения x = 0
result_substituted = result.subs(x, 0)

# Проверка каждого элемента матрицы
solutions = []
for element in result_substituted:
    poly_y = sp.Poly(element, y)
    roots_y = poly_y.nroots()
    poly_z = sp.Poly(element, z)
    roots_z = poly_z.nroots()
    solutions.append((roots_y, roots_z))

# Вывод решений
for solution in solutions:
    print(solution)
