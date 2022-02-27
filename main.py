import math


def main():
    x_min = 0.01
    x_max = 0.06

    print()

    division()

    print("|\t  x\t\t|\tPython's function\t|\tMy function\t\t\t|\t\t\tΔf\t\t\t\t|")

    division()

    while x_min <= x_max:
        df = pythons_functions(x_min) - own_function(x_min)
        print("|\t" + round(x_min, 3).__str__() + "\t|\t" + pythons_functions(x_min).__str__() + "\t|\t" + own_function(x_min).__str__() + "\t|\t" + df.__str__() + "\t|")
        x_min += 0.005

    division()



def division():
    print("*-----------*-----------------------*-----------------------*---------------------------*")


def pythons_functions(x: float):
    return math.exp(1 + x) * math.cos(math.sqrt(1 + x))


def own_function(x: float):
    return own_exp(1 + x) * own_cos(own_sqrt(x+1))


def own_exp(x: float):
    k = 0
    y = 0.0
    # eps = 0.0001
    while k < 15:
        y += x ** k / math.factorial(k)
        k += 1
    return y


def own_cos(x: float):
    k = 0
    y = 0.0
    # eps = 0.0001
    while k < 10:
        y += ((-1) ** k) * (x ** (2 * k) / math.factorial(2 * k))
        k += 1
    return y


def own_sqrt(x: float):
    k = 0
    y = 1.0
    # eps = 0.0001
    while k < 10:
        y = 0.5 * (y + x/y)
        k += 1
    return y


main()
