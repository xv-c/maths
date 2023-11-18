from sympy import symbols, Eq, Matrix, solve
from sympy.solvers.inequalities import reduce_rational_inequalities

# Создание символьных переменных
x, y, z = symbols('x y z')

# Создание матрицы
A = Matrix([
    [-0.192307692, 0.230769231, 0],
    [0.230769231, -0.076923077, 0],
    [0.846153846, -1.615384615, 1],
])

# Создание столбца с неизвестными
X = Matrix([[x + 3900], [y + 4940], [z + 5120]])

B = Matrix([[0], [0], [0]])
# Уравнение A * X = B
equation = Eq(A * X, B)
equations_text = [str(eq) for eq in equation.lhs]

# Вывод уравнений
for eq in equations_text:
    print(eq)

print()

print()
print("z != 0")
for eq in equation.lhs:
    subsed = eq.subs(x, 0).subs(y, 0)
    print(subsed)

print()
print("y != 0")
for eq in equation.lhs:
    subsed = eq.subs(x, 0).subs(z, 0)
    print(subsed)

print()
print("x != 0")
subsed = []
for eq in equation.lhs:
    subsed = eq.subs(y, 0).subs(z, 0)
    reduced = reduce_rational_inequalities([[subsed >= 0]], x)
    print(reduced)
