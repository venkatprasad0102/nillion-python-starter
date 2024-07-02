from nada_dsl import *


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute the greatest common divisor of my_int1 and my_int2
    gcd_result = gcd(my_int1, my_int2)

    # Return the result as the output
    return [Output(gcd_result, "gcd_output", party1)]

