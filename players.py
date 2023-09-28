def open_or_senior(data):
    return ['Senior' if player[0] >= 55 and player[1] > 7
            else 'Open' for player in data]

# Best Practice
# def openOrSenior(data):
#   return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]


output = open_or_senior([(45, 12), (55, 21), (19, -2),
                         (104, 20)])

print(output)

assert output == ['Open', 'Senior', 'Open', 'Senior']
