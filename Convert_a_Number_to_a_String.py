import logging

log = logging.Logger(__name__)


def number_to_string(num: int) -> str:
    if type(num) in (int, float):
        return str(num)
    return AssertionError(f'{type(num)} <- is not a number')


if __name__ == '__main__':
    type_of_response = type(number_to_string({}))
    log.info(type_of_response)
    try:
        assert type_of_response == str
    except AssertionError:
        log.error('wrong type of input data')
