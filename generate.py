import random

# generates the password


def generate(words, caps, numbers, symbols):
    # first checks to see if the arguments are valid,
    # which means the number of words is not exceeded by any other argument.
    if caps > words or numbers > words or symbols > words:
        raise ValueError(
            "number of caps, numbers, or symbols cannot exceed number of words")

    password = []

    symbolList = ["~", "!", "@", "#", "$", "%", "^", "&", "*", ".", ":", ";"]

    with open("words.txt") as f:
        lines = f.readlines()
        for i in range(0, words):
            randomIndex = random.randint(0, len(lines) - 1)
            randomWord = lines[randomIndex][0: len(lines[randomIndex]) - 1]
            password.append(randomWord)
    f.close()

    # caps
    for i in range(0, caps):
        password[i] = password[i].capitalize()

    # shuffle
    random.shuffle(password)

    # numbers
    for i in range(0, numbers):
        randomNumber = random.randint(0, 9)
        password[i] = str(randomNumber) + password[i]

    # shuffle
    random.shuffle(password)

    # symbols
    for i in range(0, symbols):
        randomIndex = random.randint(0, len(symbolList) - 1)
        password[i] = password[i] + symbolList[randomIndex]

    # shuffle
    random.shuffle(password)

    # add all the words together
    result = "".join(password)
    return result
