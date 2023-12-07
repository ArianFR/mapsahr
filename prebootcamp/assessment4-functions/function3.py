def prime_factors_sum(number):
    factors = set()
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            factors.add(divisor)
            number = number // divisor
        else:
            divisor += 1

    return sum(factors)

def digits_sum(number):
    return sum(int(digit) for digit in str(number))

def do_the_math(number):
    for i in range(number):
        p = prime_factors_sum(i)
        d = digits_sum(i)
        pedar = i + p + d
        if number == pedar:
            return pedar
    return 'no'


def fother_finder():
    t = int(input('How many inputs?: '))
    for _ in range(t):
        input_number = int(input('Give me your actual number: '))
        result = do_the_math(input_number)
        if result != 'no':
            print('Yes')
        else:
            print('No')


fother_finder()
