numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers[1:15]:
    for j in range(2, i):
        is_prime = i % j > 0
        if not is_prime:
            not_primes.append(i)
            break
    if is_prime:
        primes.append(i)
    continue
print(primes)
print(not_primes)