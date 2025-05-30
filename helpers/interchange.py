
import random

def interchange_mutation(sequence):

    length = len(sequence) - 2
    point1 = random.randint(1, length)
    point2 = random.randint(1, length)

    sequence[point1], sequence[point2] = sequence[point2], sequence[point1]

    return sequence