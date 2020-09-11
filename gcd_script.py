def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

if __name__ == "__main__":

    if gcd(40,12)==4:
        print("Everything is OK")
    else:
        print("The GCD function is wrong")
