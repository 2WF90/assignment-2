def find_divisors(num: int) -> list[int]:
    div = []

    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            div.append(i)
            div.append(num // i)
    
    if div[-1] == div[-2]:
        div.pop()

    div.sort()

    return div
