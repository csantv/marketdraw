import random
import hashlib
from decimal import Decimal


def main():
    # values = [
    #     Decimal("0.2505"),  # allocation_percentage
    #     Decimal("13.30"),  # last_price
    #     Decimal("-36.97"),  # unrealized_gain
    #     Decimal("-16.00"),  # daily_gain
    # ]

    # values = [
    #     Decimal("0.2681"),  # allocation_percentage
    #     Decimal("5.1"),     # last_price
    #     Decimal("383.99"),  # unrealized_gain
    #     Decimal("0"),       # daily_gain
    # ]

    values = [
        Decimal("0.2320"),   # allocation_percentage
        Decimal("6.800"),    # last_price
        Decimal("-148.77"),  # unrealized_gain
        Decimal("0"),        # daily_gain
    ]
    print(extract_numbers(values, 35))

def reduce_number(number: int, max_number: int) -> int:
    if max_number < 1:
        raise ValueError("max_number must be positive")

    while number > max_number:
        number = sum(map(int, str(number)))

    return number

def extract_numbers(values: list[Decimal], max_number: int, min_number = 1) -> list[int]:
    numbers = set()

    for value in values:
        digits = ''.join(
            char for char in format(abs(value), 'f')
            if char.isdigit()
        )

        for i in range(len(digits) - 1):
            number = int(digits[i:i + 2])
            number = reduce_number(number, max_number)

            if min_number <= number <= max_number:
                numbers.add(number)

    seed_data = f"{min_number}:{max_number}:{','.join(map(str, values))}"
    seed = int.from_bytes(hashlib.sha256(seed_data.encode()).digest())

    result = sorted(numbers)
    rng = random.Random(seed)
    rng.shuffle(result)
    return result
