#!/usr/local/bin/python3
# Written for Python 3.7.5+
# Requires matplotlib library

import sys
import matplotlib.pyplot as plt

print('----------')
print('| Corona |')
print('----------')

FACTOR = 2
INITIAL = 0
GENERATIONS = 10

generations = []
gen_y = 0
gen_z = 0


def main():
    """
    Demonstrates the infection rate of Coronavirus over generations of spread

    Accepts 2 arguments or 0 (uses defaults).

    Arguments:
        infection_factor: defaults to 2
        generations_count: defaults to 10
    """
    global new_infections
    global gen_y
    global gen_z

    print('Infection Factor:', infection_factor)
    print('Generations Count:', generations_count)

    if len(sys.argv) == 3:
        # get rid of command path in args
        sys.argv.pop(0)
        # get the command line values
        infection_factor = float(sys.argv.pop(0))  # get 1
        generations_count = int(sys.argv.pop(0))  # get 2
    elif ((len(sys.argv) > 1) and (len(sys.argv) != 3)):
        print("Error: incorrect number of arguments.")
        exit()
    else:
        # 0 parameters, so assume defaults
        infection_factor = FACTOR
        generations_count = GENERATIONS

    new_infections = 0
    gen_y = 0
    gen_z = 1

    for gen in range(INITIAL, generations_count):
        print('----------')
        #print('gen_y:', gen_y)
        #print('gen_z:', gen_z)

        if gen > 0:
            new_infections = (gen_z - gen_y) * infection_factor
            gen_y = gen_z
            gen_z = gen_y + new_infections

        generations.insert(gen, gen_z)
        #print('Generation ', gen, ': ', generations, sep="")
        print('Generation', gen)
        print('   New Infections:', new_infections)
        print('   Total Infections:', gen_z)
        print('----------')

    x = [*range(0, len(generations))]
    y = generations

    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()
