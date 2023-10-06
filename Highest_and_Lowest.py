numbers_as_str = '1 2 3'


def high_and_low(numbers: str) -> (int, int):
    numbers_as_list = [int(x) for x in numbers.split()]
    return f'{max(numbers_as_list)} {min(numbers_as_list)}'


print(high_and_low(numbers_as_str))
