
import random

def initial_population(STARTER_CITY, POPULATION, NUM_CITIES):
    init_pop = []
    for i in range(POPULATION):
        curr = []
        added_cities = set()
        curr.append(STARTER_CITY)
        added_cities.add(STARTER_CITY)

        while len(added_cities) != 10:
            city = random.randrange(0, NUM_CITIES)
            if not city in added_cities:
                curr.append(city)
                added_cities.add(city)

        curr.append(STARTER_CITY)
        init_pop.append(curr)
    
    return init_pop
