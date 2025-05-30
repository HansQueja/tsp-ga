
import random

def order_crossover(sequence1, sequence2, start_city):

    indices = set()
    new_sequence1 = []
    new_sequence2 = []
    added_cities = set()

    length = len(sequence1) - 2
    point1 = random.randint(1, length - 1)
    point2 = random.randint(point1 + 1, length)

    # Do first child

    new_sequence1.append(start_city)
    
    for city in sequence1[point1:point2]:
        new_sequence1.append(city)
        added_cities.add(city)

    for city in sequence2:
        if city != start_city and not city in added_cities:
            new_sequence1.append(city)
            added_cities.add(city)
    
    new_sequence1.append(start_city)

    added_cities = set()

    # Do second child
    new_sequence2.append(start_city)
    
    for city in sequence2[point1:point2]:
        new_sequence2.append(city)
        added_cities.add(city)

    for city in sequence1:
        if city != start_city and not city in added_cities:
            new_sequence2.append(city)
            added_cities.add(city)
    
    new_sequence2.append(start_city)

    return new_sequence1, new_sequence2