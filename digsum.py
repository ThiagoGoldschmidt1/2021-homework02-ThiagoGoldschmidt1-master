""" Script that provides digit sum functionality. """

def main():

    print("digsum(0) =", digsum(0))
    print("digsum(12) =", digsum(12))
    print("digsum(333) =", digsum(333))
    print("digsum(9173) =", digsum(9173))


def digsum(num):
    """ This function returns the digit sum of a given int number. """
    # delete the line below this and insert your own code
    sum_of_digits = 0
    num = str(num)

    for digit in num:
        sum_of_digits += int(digit)

    return sum_of_digits



if __name__ == "__main__":
    main()
