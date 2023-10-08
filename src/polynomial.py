class Polynomial:
    def __init__(self, exponents: list[int]):
        self.exponents = exponents

    def __len__(self) -> int:
        return len(self.exponents)

    def __getitem__(self, key: int) -> int:
        return self.exponents[key]

    def get_exponents(self) -> list[int]:
        return self.exponents
    
    def get_sanitized(self):
        for i in range(len(self.exponents) - 1, -1, -1):
            if self.exponents[i] != 0:
                return self.exponents[:i + 1]
        return list()