
class Permutation:
    def __init__(self, sequence, fitness=0):
        self.sequence = sequence
        self.fitness = fitness

    def __str__(self):
        return f"Sequence: {self.sequence}, Fitness: {self.fitness}"