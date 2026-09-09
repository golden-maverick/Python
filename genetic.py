import random

#Genetic Algorithm parameters
POPULATION_SIZE = 6
CHROMOSOME_LENGTH = 5
MUTATION_RATE = 0.1
GENERATIONS = 10

# Createa random chromosome
def create_chromosome():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]

# Covert binary chromosome to decimal
def chromosome_to_x(chromosome):
    binary = ''.join(map(str, chromosome))
    return int(binary, 2)

# Fitness function : f(x) = x^2
def fitness(chromosome):
    x = chromosome_to_x(chromosome)
    return x *x

# Selection : select the two best chromosomes
def selection(population):
    population.sort(key=fitness, reverse=True)
    return population[:2]

# Crossover : create childdren from two parents
def crossover(parent1, parent2):
        point = random.randint(1, CHROMOSOME_LENGTH - 1)

        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2

# Mutation : randomly change a bit in the chromosome
def mutation(chromosome):
     for i in range(CHROMOSOME_LENGTH):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]  # Flip the bit 

        return chromosome  

# Create initial population
population = [create_chromosome() for _ in range(POPULATION_SIZE)]

# Genetic Algorithm
for generation in range(GENERATIONS):
# Select best parents
    parents = selection(population)

    # Create new population
    new_population = parents.copy()

    while len(new_population) < POPULATION_SIZE:
      parent1= random.choice(parents)
      parent2= random.choice(parents)

      child1, child2 = crossover(parent1, parent2)

      child1 = mutation(child1)
      child2 = mutation(child2) 

      new_population.append(child1)

      if len(new_population) < POPULATION_SIZE:
          new_population.append(child2)
    population = new_population

    # Display best solution
    best= max(population, key=fitness)

    print(
            "Generation:", generation + 1,
            "Best Chromosome:", ''.join(map(str, best)),
            "x =", chromosome_to_x(best),
            "Fitness =", fitness(best)
        )

# Final result
best = max(population, key=fitness)

print("\nFinal Best Solution")
print("Chromosome:", ''.join(map(str, best)))
print("x =", chromosome_to_x(best))
print("Maximum value =", fitness(best))
     

      
     
          




