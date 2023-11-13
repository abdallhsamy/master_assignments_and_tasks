## Assignment 1

### Question 
Apply Laws of Evolution on your own simple python program (you can use any programming language)

### Answer
Evolutionary principles can be applied in various ways to create programs that learn and adapt. Let's consider a simple example using a genetic algorithm in Python to optimize a basic mathematical function.

We'll aim to find the maximum value of the function 
<span id="example-problem"><span class="MathJax_Preview" style="color: inherit;"></span><span id="MathJax-Element-1-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 113%; position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mstyle displaystyle=&quot;true&quot;><mi>f</mi><mrow><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>4</mn></mstyle></math>" role="presentation"><span id="MJXc-Node-1" class="mjx-math" aria-hidden="true"><span id="MJXc-Node-2" class="mjx-mrow"><span id="MJXc-Node-3" class="mjx-mstyle"><span id="MJXc-Node-4" class="mjx-mrow"><span id="MJXc-Node-5" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.481em; padding-bottom: 0.481em; padding-right: 0.06em;">f</span></span><span id="MJXc-Node-6" class="mjx-mrow MJXc-space1"><span id="MJXc-Node-7" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.481em; padding-bottom: 0.592em;">(</span></span><span id="MJXc-Node-8" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.223em; padding-bottom: 0.297em;">x</span></span><span id="MJXc-Node-9" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.481em; padding-bottom: 0.592em;">)</span></span></span><span id="MJXc-Node-10" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.076em; padding-bottom: 0.334em;">=</span></span><span id="MJXc-Node-11" class="mjx-msup MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-12" class="mjx-mrow"><span id="MJXc-Node-13" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.223em; padding-bottom: 0.297em;">x</span></span></span></span><span class="mjx-sup" style="font-size: 70.7%; vertical-align: 0.584em; padding-left: 0px; padding-right: 0.071em;"><span id="MJXc-Node-14" class="mjx-mrow" style=""><span id="MJXc-Node-15" class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.371em; padding-bottom: 0.334em;">2</span></span></span></span></span><span id="MJXc-Node-16" class="mjx-mo MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.297em; padding-bottom: 0.407em;">−</span></span><span id="MJXc-Node-17" class="mjx-mn MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.407em; padding-bottom: 0.334em;">4</span></span><span id="MJXc-Node-18" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.223em; padding-bottom: 0.297em;">x</span></span><span id="MJXc-Node-19" class="mjx-mo MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.297em; padding-bottom: 0.407em;">−</span></span><span id="MJXc-Node-20" class="mjx-mn MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.407em; padding-bottom: 0.334em;">4</span></span></span></span></span></span><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mstyle displaystyle="true"><mi>f</mi><mrow><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>4</mn></mstyle></math></span></span><script type="math/mml" id="MathJax-Element-1"><math><mstyle displaystyle="true"><mi>f</mi><mrow><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>4</mn></mstyle></math></script></span> 

Our genetic algorithm will evolve a population of potential solutions to converge toward the maximum of this function.

Here's a basic implementation using a genetic algorithm:

```python
import random

# Function to evaluate fitness
def fitness_function(x):
    return x**2 - 4*x + 4  # f(x) = x^2 - 4x + 4

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

```

In this code, a population of potential solutions (randomly chosen x values) is created and then evolved over multiple generations. The algorithm uses selection, crossover, and mutation to simulate the principles of evolution.

The program tries to find the value of 'x' that maximizes the function 
<span id="example-problem"><span class="MathJax_Preview" style="color: inherit;"></span><span id="MathJax-Element-1-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 113%; position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mstyle displaystyle=&quot;true&quot;><mi>f</mi><mrow><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>4</mn></mstyle></math>" role="presentation"><span id="MJXc-Node-1" class="mjx-math" aria-hidden="true"><span id="MJXc-Node-2" class="mjx-mrow"><span id="MJXc-Node-3" class="mjx-mstyle"><span id="MJXc-Node-4" class="mjx-mrow"><span id="MJXc-Node-5" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.481em; padding-bottom: 0.481em; padding-right: 0.06em;">f</span></span><span id="MJXc-Node-6" class="mjx-mrow MJXc-space1"><span id="MJXc-Node-7" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.481em; padding-bottom: 0.592em;">(</span></span><span id="MJXc-Node-8" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.223em; padding-bottom: 0.297em;">x</span></span><span id="MJXc-Node-9" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.481em; padding-bottom: 0.592em;">)</span></span></span><span id="MJXc-Node-10" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.076em; padding-bottom: 0.334em;">=</span></span><span id="MJXc-Node-11" class="mjx-msup MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-12" class="mjx-mrow"><span id="MJXc-Node-13" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.223em; padding-bottom: 0.297em;">x</span></span></span></span><span class="mjx-sup" style="font-size: 70.7%; vertical-align: 0.584em; padding-left: 0px; padding-right: 0.071em;"><span id="MJXc-Node-14" class="mjx-mrow" style=""><span id="MJXc-Node-15" class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.371em; padding-bottom: 0.334em;">2</span></span></span></span></span><span id="MJXc-Node-16" class="mjx-mo MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.297em; padding-bottom: 0.407em;">−</span></span><span id="MJXc-Node-17" class="mjx-mn MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.407em; padding-bottom: 0.334em;">4</span></span><span id="MJXc-Node-18" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.223em; padding-bottom: 0.297em;">x</span></span><span id="MJXc-Node-19" class="mjx-mo MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.297em; padding-bottom: 0.407em;">−</span></span><span id="MJXc-Node-20" class="mjx-mn MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.407em; padding-bottom: 0.334em;">4</span></span></span></span></span></span><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mstyle displaystyle="true"><mi>f</mi><mrow><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>4</mn></mstyle></math></span></span><script type="math/mml" id="MathJax-Element-1"><math><mstyle displaystyle="true"><mi>f</mi><mrow><mo>(</mo><mi>x</mi><mo>)</mo></mrow><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>4</mn></mstyle></math></script></span> 

The 'genetic_algorithm' function performs the evolution process to achieve this. The final result should give the 'x' value where the function reaches its maximum.