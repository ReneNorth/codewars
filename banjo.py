
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo"
# name + " does not play banjo"
# Names given are always valid strings.

name1 = 'rick'
name2 = 'Rick'
name3 = 'Morty'


def are_you_playing_banjo(name):
    match name:
        case name if name.startswith('R') | name.startswith('r'):
            return f'{name} plays banjo'
        case _:
            return f'{name} does not play banjo'


if __name__ == '__main__':
    assert are_you_playing_banjo(name1) == f'{name1} plays banjo'
    assert are_you_playing_banjo(name2) == f'{name2} plays banjo'
    assert are_you_playing_banjo(name3) == f'{name3} does not play banjo'
