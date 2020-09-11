def test():
    prod = 1
    for i in range(0, 10):
        prod *= i / (i - 5)
    print(prod)
