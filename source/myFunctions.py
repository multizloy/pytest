def add(numberOne, numberTwo):
    return numberOne + numberTwo


def divide(numberOne, numberTwo):
    if numberTwo == 0:
        raise ValueError
    return numberOne / numberTwo
