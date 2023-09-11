arr = [[10, 0], [3, 5], [5, 8]]


def numbers(bus_stops):
    count = 0
    for stop in bus_stops:
        count += stop[0]
        count -= stop[1]
    return count


def main():
    return numbers(arr)


if __name__ == '__main__':
    res = main()
    assert res, 5
    print(res)
