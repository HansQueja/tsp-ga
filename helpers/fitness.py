

def fitness_func(sequence, dist_matrix):
    total_distance = 0

    for i in range(len(sequence) - 1):
        curr_city = sequence[i]
        next_city = sequence[i + 1]

        total_distance += dist_matrix[curr_city][next_city]
    
    return total_distance