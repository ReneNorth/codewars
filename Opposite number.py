import logging

log = logging.getLogger(__name__)


def make_negative(num: int | float):
    try:
        return -abs(num)
    except TypeError:
        return None


def main():
    return make_negative('asd')


if __name__ == "__main__":
    print(main())
