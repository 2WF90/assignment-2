def gen_primes(num: int) -> list[int]:
    num = num + 1
    sieve = [True for _ in range(num)]
    primes = [2]

    for n in range(3, num, 2):
        if sieve[n - 1]:
            primes.append(n)
            for i in range(n - 1, num, n):
                sieve[i] = False
    
    return primes

def filter_divisors(num: int, potential_divisors: list[int]) -> list[int]:
    return [p for p in potential_divisors if num % p == 0]