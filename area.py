from sympy import symbols, Eq, Matrix

# Создание символьных переменных
x, y = symbols('x y z')

# Создание матрицы
A = Matrix([[1, 2], [0, 0]])

# Создание столбца с неизвестными
X = Matrix([[x], [y]])

# Уравнение A * X = B
equation = Eq(A * X, X)

print(equation)