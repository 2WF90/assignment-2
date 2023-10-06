class Polynomial:
    def __init__(self, exponents: list[int]):
        self.exponents = exponents

    def __len__(self) -> int:
        return len(self.exponents)

    def __getitem__(self, key) -> int:
        return self.exponents[key]

    def get_exponents(self) -> list[int]:
        return self.exponents