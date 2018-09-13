import random
import math



def prime_test(N, k):
    # You will need to implements this function and change the return value.

    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.

	# Remember to ensure that all of your random values are unique

    # Should return one of three values: 'prime', 'composite', or 'carmichael'

	#random_value = generate random(low. hi)
	#random_value in seed
	#if false then add to seed otherwise then go again
	#then keep using it on whatever it is

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
