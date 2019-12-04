def factorial(numf, fact, i):

    numf = int(input("Ingrese número a factorizar --> "))

    while i <= numf:
        yield fact * i

        fact = fact*i

        i += 1

    print(f"{numf}!={fact}")


calculoF = factorial(2, 1, 1)

print(next(calculoF))
print(next(calculoF))
print(next(calculoF))
print(next(calculoF))
