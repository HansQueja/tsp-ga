
import random

def tournament(population, tournament_size=3):

    tournament_individuals = random.choices(population, k=tournament_size)

    best_individual = min(tournament_individuals, key=lambda individual: individual.fitness)

    return best_individual