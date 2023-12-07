import random

x = [0]*3
y = [0]*3
r = [0]*3
rr = [0]*3

for j in range(3):
    print(f'{j+1}-я окружность (x y r): ')
    x[j], y[j], r[j] = map(float, input().split())
    rr[j] = r[j]**2

n = int(input('Количество историй: '))

xmin = x[0] - r[0]
ymin = y[0] - r[0]
d = r[0] * 2
m = 0

for i in range(n):
    # Randomly throw points into the selected square
    xp = random.random() * d + xmin
    yp = random.random() * d + ymin

    # Check if the point falls into each circle
    for j in range(3):
        if (xp - x[j])**2 + (yp - y[j])**2 > rr[j]:
            break
    else:
        # Count the number of points that hit all three circles at once
        m += 1

# The result is more accurate the more stories
print(f'S={d**2 * m / n:.3f}')