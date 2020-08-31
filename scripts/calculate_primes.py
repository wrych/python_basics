import sys


def print_all_primes_under(max_value):
    pass


def checking_primes(input_number):
    for n in range(2, input_number):
        if input_number % n == 0:
            return False
    else:
        return True


def main():
    max_value = sys.argv[1]
    print_all_primes_under(max_value)


if __name__ == "__main__":
    main()
