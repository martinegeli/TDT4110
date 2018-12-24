
def multiplikasjon(tol):
    counter = 1
    prod = 1 + 1/(counter**2)
    old_prod = 0
    diff = prod - old_prod
    while diff > tol:
        old_prod = prod
        counter += 1
        prod *= (1 + 1/(counter**2))
        diff = prod-old_prod
    return counter, diff, prod

print(multiplikasjon(0.01))

