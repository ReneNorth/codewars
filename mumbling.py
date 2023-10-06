# accum("abcd") -> "A-Bb-Ccc-Dddd"

test_str = 'abcd'


def capitalizer(letters: str) -> str:
    return letters.capitalize()


def accum(s):
    return '-'.join(map(
        capitalizer, [char * (i+1) for i, char in enumerate(s)]))

# best practice
# def accum(s):
    # return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


print(accum(test_str))
