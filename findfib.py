""" Script that finds the first Fibonacci number that has a digit sum higher than 42. """

from fibonacci import fibonacci
from digsum import digsum

def main():

    print("findfib() returns", findfib())


def findfib():
    """ This function returns the first Fibonacci number that has a digit sum higher than 42. """

    # delete the line below this and insert your own code
    for num in range(1,1000):
        fib_num = fibonacci(num)
        if digsum(fib_num) > 42:
            return fib_num
            break



if __name__ == "__main__":
    main()
