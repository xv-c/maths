def mixed_congruential_generator(mu, lambda_, m, y0, count):
    numbers = []
    y = y0
    for _ in range(count):
        y = (mu + lambda_ * y) % m
        numbers.append(y)
    return numbers

mu = 1
lambda_ = 5
m = 16
y0 = 3

generated_numbers = mixed_congruential_generator(mu, lambda_, m, y0, 20)
print(generated_numbers)