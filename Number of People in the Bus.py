arr = [[10, 0], [3, 5], [5, 8]]


def numbers(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])


def main():
    return numbers(arr)


if __name__ == '__main__':
    res = main()
    assert res, 5
    print(res)
