from random import randint

N = 1000


def simulate(N):
    K = 0

    for _ in range(N):

        truth = randint(1, 3)
        guess = randint(1, 3)

        if truth == guess:
            monte = randint(1, 3)
            while monte == truth:
                monte = randint(1, 3)
        else:
            monte = 6 - truth - guess

        guess2 = 6 - guess - monte
        if guess2 == truth:
            K += 1

    return float(K) / float(N)

print(simulate(N))
