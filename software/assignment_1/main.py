import random


# Function to evaluate fitness
def fitness_function(x):
    return x ** 2 - 4 * x + 4  # f(x) = x^2 - 4x + 4


# Function to create an initial population
def create_population(size):
    return [random.uniform(-10, 10) for _ in range(size)]


# Function to select parents for breeding
def select_parents(population):
    return random.choices(population, k=2, weights=[fitness_function(x) for x in population])


# Function for crossover (breeding)
def crossover(parents):
    return (parents[0] + parents[1]) / 2


# Function for mutation
def mutate(child):
    mutation_rate = 0.1
    if random.random() < mutation_rate:
        child += random.uniform(-1, 1)
    return child


# Genetic algorithm
def genetic_algorithm():
    population_size = 20
    generations = 50

    population = create_population(population_size)

    for generation in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parents = select_parents(population)
            child = crossover(parents)
            child = mutate(child)
            new_population.extend([child, parents[0]])

        population = new_population

    # Finding the best individual after all generations
    best_individual = max(population, key=fitness_function)
    return best_individual


# Running the genetic algorithm and obtaining the result
result = genetic_algorithm()
print("The maximum value of the function is:", fitness_function(result), "at x =", result)
