import random
import math



def prime_test(N, NUMBER_OF_ATTEMPTS):
    # You will need to implements this function and change the return value.
    EMPTY = 0
    lowest = 1
    highest = N-1
    set_of_numbers = set()
    iterations = 0

    while (len(set_of_numbers) == EMPTY or random_value in set_of_numbers) and (iterations <= NUMBER_OF_ATTEMPTS) :

        random_value = random.randint(lowest,highest)
		#DO THE REST OF LOGIC IN HERE

        if not random_value in set_of_numbers :
			set_of_numbers.add(random_value)
			iterations += 1

    # Should return one of three values: 'prime', 'composite', or 'carmichael'

	return 'prime'


def mod_exp(x,y,n):

    if y == 0 : return 1
    z = mod_exp(x, math.floor(y/2), n)

    #checking if y is even
    if y % 2 == 0:
        return (z**2) % n
    else:
        return x*(z**2) % n


def probability(k):
    return 1 - ((1/2)**k)


def is_carmichael(N,a):
	#testubg cinnubg
    # You will need to implements this function and change the return value.

	return False
