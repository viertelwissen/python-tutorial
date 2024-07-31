import enum
import math


class Rechenoperation(enum.Enum):
    ADDITION = enum.auto()
    SUBTRACTION = enum.auto()
    MULTIPLICATION = enum.auto()
    DIVISION = enum.auto()


def berechnung(operator: Rechenoperation, *allezahlen: int) -> int:
    if len(allezahlen) == 1:
        return allezahlen[0]

    match operator:
        case Rechenoperation.ADDITION:
            summe = sum(allezahlen)
        case Rechenoperation.MULTIPLICATION:
            summe = math.prod(allezahlen)
        case _:
            raise ValueError("Da hat etwas nicht geklappt.")
    return summe


print(berechnung(Rechenoperation.MULTIPLICATION, 5, 20, 34, 12, 4))
print(berechnung(Rechenoperation.ADDITION, 5))
print(berechnung("LUL", 234, 57, 457))
