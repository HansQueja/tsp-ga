
import random
import time

from helpers.parser import parser
from helpers.population import initial_population
from helpers.fitness import fitness_func
from helpers.tournament import tournament
from helpers.order_crossover import order_crossover
from helpers.interchange import interchange_mutation

from permutation import Permutation

STARTER_CITY = 0
POPULATION = 100
NUM_CITIES = 10
GENERATION = 100

def main():
    dist_matrix = parser()

    # Initialize the population
    init_population = initial_population(STARTER_CITY, POPULATION, NUM_CITIES)
    current_population = []

    for sequence in init_population:
        fitness = fitness_func(sequence, dist_matrix)
        permutation = Permutation(sequence, fitness)
        current_population.append(permutation)
    
    # Best solution is here
    best_solution = min(current_population, key=lambda x: x.fitness)

    print("+-------------+-------------------------------------------------+-------------+------------------+")
    print("| Generation  | Proposed Coordinates                            | Cost Value  | Response Time (s)|")
    print("+-------------+-------------------------------------------------+-------------+------------------+")

    for generation in range(GENERATION):
        start_time = time.time() 
        new_population = []

        while len(new_population) < POPULATION:
            # Select parents using tournament selection
            parent1 = tournament(current_population, 3)
            parent2 = tournament(current_population, 3)

            # Crossover the two parents!
            child1, child2 = order_crossover(parent1.sequence, parent2.sequence, STARTER_CITY)

            # Do mutation based on probability
            if random.random() < 0.1:
                child1 = interchange_mutation(child1)
            if random.random() < 0.1:
                child2 = interchange_mutation(child2)

            # Evaluate their fitness
            fitness1 = fitness_func(child1, dist_matrix)
            fitness2 = fitness_func(child2, dist_matrix)

            new_population.append(Permutation(child1, fitness1))
            if len(new_population) < POPULATION:
                new_population.append(Permutation(child2, fitness2))
        
        current_population = new_population

        # Monitor which is the best solution
        generation_best = min(current_population, key=lambda x: x.fitness)
        if generation_best.fitness < best_solution.fitness:
            best_solution = generation_best

        end_time = time.time()
        response_time = round(end_time - start_time, 4)
        
        print(f"| {generation:<11} | ({generation_best.sequence})           | {round(generation_best.fitness, 3):<11} | {response_time:<18} |")

    print("+-------------+-------------------------------------------------+-------------+------------------+")
    print(f"Final best solution: {best_solution.sequence}")
    print(f"Final best fitness: {best_solution.fitness}")

if __name__ == "__main__":
    main()
