def compute_spf(n: int):
    spf = list(range(n + 1))  # spf[x] = smallest prime factor of x
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:  # i is prime
            for j in range(i * i, n + 1, i):
                if spf[j] == j:  # not marked yet
                    spf[j] = i
    return spf


# Example usage
N = 100
spf = compute_spf(N)
print(spf)
print("SPF of numbers 2..100:")
for i in range(2, 100):
    print(i, "->", spf[i])


def factorize(x, spf):
    factors = []
    while x != 1:
        factors.append(spf[x])
        x //= spf[x]
    return factors

def factor_distinct_primes(x, spf):
    ps = set()
    while x > 1:
        p = spf[x]
        ps.add(p)
        while x % p == 0:   # skip all multiples of the same prime
            x //= p
    return ps

# Example
print(factorize(84, spf))  # [2, 2, 3, 7]
print(factor_distinct_primes(84, spf))  # [2, 3, 7]
print(factor_distinct_primes(12, spf))  # [2, 3, 7]
