import random

def monte_carlo(N):
    N1 = 0
    for i in range(N):
        x = 2 * random.random()
        y = 2 * random.random()
        if (x - 1)**2 + (y - 1)**2 <= 1:
            N1 += 1
    Pi = 4 * N1 / N
    return Pi

for k in range(2):
    N = int(input('N='))
    print(k+1, end=' ')
    Sr = 0
    for j in range(10):
        Pi = monte_carlo(N)
        print(f'{Pi:.4f}', end=' ')
        Sr += Pi / 10
    print()
    print(f'Srednee Pi={Sr:.4f}')