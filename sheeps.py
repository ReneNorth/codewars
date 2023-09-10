
sheeps = [True,  True,  True,  False,
          True,  True,  True,  True,
          True,  False, True,  False,
          True,  False, False, True,
          True,  True,  True,  True,
          False, False, True,  True]


def count_missing(sheeps):
    return len(sheeps) - len([sheep for sheep in sheeps if not sheep])


def main():
    return count_missing(sheeps)


if __name__ == '__main__':
    result = main()
    assert result, 17
    print(result)
