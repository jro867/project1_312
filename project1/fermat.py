import random
import math

def prime_test(N, k):
    return run_fermat(N,k), run_miller_rabin(N,k)
    # lowest = 1
    # highest = N-1
    # set_of_numbers = set()
    # iterations = 1
    # carmichael = 0
    # result = 'prime'
    #
    # while (iterations <= NUMBER_OF_ATTEMPTS) :
    #     #O(k(O^4))
    #     random_value = random.randint(lowest,highest)
    #     if not random_value in set_of_numbers :
    #
    #         set_of_numbers.add(random_value)
    #         print('iterations ', iterations)
    #         iterations += 1
    #         fermat = mod_exp(random_value, highest, N)
    #
    #         print('fermat value: ', fermat)
    #         if fermat != 1 : return 'composite'
    #
    #         carmichael = miller_rabin_test(N, random_value)
    #         print('Carmichael value: ', carmichael)
    #         if carmichael != 1 : return 'carmichael'
    #
    # return result

def run_fermat(N,k):

    lowest = 1
    highest = N-1
    set_of_numbers = set()
    iterations = 1
    carmichael = 0
    result = 'prime'

    while (iterations <= k) :
        #O(k(O^4))
        random_value = random.randint(lowest,highest)
        if not random_value in set_of_numbers :

            set_of_numbers.add(random_value)
            print('iterations ', iterations)
            iterations += 1
            fermat = mod_exp(random_value, highest, N)

            print('fermat value: ', fermat)
            if fermat != 1 : return 'composite'

    return result


#3 Code the probability that k Fermat trials gave you the correct answer -- see the discussion between Figure 1.7 and Figure 1.8.
#WHERE should I put this

#4 Implement the Miller-Rabin primality test. There is no pseudo-code in the book for this, but you can find what you need in the sidebar on p. 28 and in the discussion that follows.

#this is #2 from the instructions. Figure 1.4 p. 19
def mod_exp(x,y,n): #O(n^3)

    if y == 0 : return 1
    z = mod_exp(x, math.floor(y/2), n) #this happens O(n) times because we are looking at this from bits point of view

    if y % 2 == 0:
        print('even:')
        return (z**2) % n #so multiplication of n bits is n2 but we are doing this n times therefore O(n^3)
    else:
        print('odd')
        return x*(z**2) % n


# def probability(k):
#     return 1 - ((1/2)**k) #constant

def run_miller_rabin(N,k):

    lowest = 1
    highest = N-1
    set_of_numbers = set()
    iterations = 1
    result = 'composite'

    n = N-1
    response = 0

    while (iterations <= k) :
        #O(k(O^4))
        random_value = random.randint(lowest,highest)
        if not random_value in set_of_numbers :

            set_of_numbers.add(random_value)
            print('iterations mr ', iterations)
            iterations += 1

            #this happens n-bit times and inside here there is the mod_exp so O(n) * O(n^3) so O(n^4)
            while ( n%2 == 0):
                print('getting here')
                n = int(n/2)
                print('new value of n: ', n)
                print('N value: ', N)
                response = mod_exp(random_value,n,N)
                print('response from miller_rabin_test: ', response)
                if response != 1 : break

            if response == 1 or response == N-1 : return 'prime'

    return result

#Checks if number is carmichael by taking the square root of a number that is equal
#to one when mod N. It does this action as long as n(which was originally N-1) is divisable by 2
# If at the end the response is anything else besides -1 and 1 then returns FALSE
#
# COMPLEXITY:
# The while loop is log(n) since it cuts n in half everythime

# def miller_rabin_test(N,a):
#
#     n = N-1
#     response = 1
#     #this happens n-bit times and inside here there is the mod_exp so O(n) * O(n^3) so O(n^4)
#     while ( n%2 == 0):
#         print('getting here')
#         n = int(n/2)
#         print('new value of n: ', n)
#         print('N value: ', N)
#         response = mod_exp(a,n,N)
#         print('response from modexp: ', response)
#         if response != 1 : break
#
#     if response > 1 and response != N-1 : return False
#     # print('Gonna return TRUE')
#     return True

def fprobability(k):
    return 1 - ((1/2)**k) #constant

def mprobability(k):
    return 1 - ((3/4)**k) #constant


# # miller_rabin_test(97,3)
# miller_rabin_test(561,4)
# # mod_exp(96,3,97)
