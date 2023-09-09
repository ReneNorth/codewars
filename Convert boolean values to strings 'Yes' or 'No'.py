# my solution
def bool_to_word1(bool):
    return "Yes" if bool else "No"


# optimal solution
def bool_to_word2(bool):
    return "Yes" if bool else "No"


# clever
def bool_to_word3(bool):
    return ["No", "Yes"][bool]
