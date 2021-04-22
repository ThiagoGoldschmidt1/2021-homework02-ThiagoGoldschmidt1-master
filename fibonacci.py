""" Script that provides Fibonacci functionality. """

def main():

    print("fibonacci(0) =", fibonacci(0))
    print("fibonacci(3) =", fibonacci(3))
    print("fibonacci(10) =", fibonacci(10))


def fibonacci(n):
    """ This function returns the nth Fibonacci number given that fibonacci(0) = 0. """

    # delete the line below this and insert your own code
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



if __name__ == "__main__":
    main()
