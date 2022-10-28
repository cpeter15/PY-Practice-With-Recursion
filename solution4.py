# Write code for algorithm 4 below

def exponents(x, y):

    if (y == 1):
        return x
    else:
        return (x * exponents(x, y-1))


print(exponents(3, 4))
