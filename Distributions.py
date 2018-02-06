def factorial(n):
    n += 1
    result = [1]*n
    # This will loop from 1 to n+1, 0! = 1
    for i in range(1, n):

        # Use the previous value of result to find answer to current problem
        result[i] = result[i-1] * i

    # Print out the result
    # for i in range(n):
    #     print(str(i) + '! = ' + str(result[i]))

    return result[-1]


def binomial_formula(n, k, p):
    first_mul = factorial(n) / (factorial(n - k) * factorial(k))
    second_mul = p**k * (1 - p)**(n-k)

    result = first_mul * second_mul

    return result

# for i in range(11):
#     print("{}: {}".format(i, binomial_formula(10, i, 0.8)))


print(1 - (binomial_formula(7, 0, 0.2) + binomial_formula(7, 1, 0.2)))