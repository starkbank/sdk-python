from random import randint, random


class TaxIdGenerator:

    @classmethod
    def taxId(cls, chance=0.5):
        if random() > chance:
            return cls.cpf()
        return cls.cnpj()

    @classmethod
    def cpf(cls):
        cpf = [randint(0, 9) for _ in range(9)]
        for _ in range(2):
            value = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11
            cpf.append(11 - value if value > 1 else 0)
        return '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*cpf)

    @classmethod
    def cnpj(cls):
        cnpj = [1, 0, 0, 0] + [randint(0, 9) for _ in range(8)]
        for _ in range(2):
            cnpj = [cls._calculateSpecialDigit(cnpj)] + cnpj
        return '{}{}.{}{}{}.{}{}{}/{}{}{}{}-{}{}'.format(*cnpj[::-1])

    @classmethod
    def _calculateSpecialDigit(cls, digits):
        digit = 0
        for index, value in enumerate(digits):
            digit += value * (index % 8 + 2)
        digit = 11 - digit % 11
        return digit if digit < 10 else 0
