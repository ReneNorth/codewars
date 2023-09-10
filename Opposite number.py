import logging

log = logging.getLogger(__name__)


def make_negative(num: int | float):
    try:
        return -(num)
    except TypeError:
        return None


def main():
    return make_negative(1)


if __name__ == "__main__":
    print(main())
