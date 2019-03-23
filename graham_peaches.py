## Note: this does not actually work in other base besides decimal

def digitsG(base, digits):
    x = 3

    for i in range(1, digits+1):
        x = pow(3, x, base ** digits)

    return x

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def lastDigitG(base):
    return baseN(digitsG(base, 600), base)[-1]

def main():
    for i in [2,3,5,7,11,13,17,19,23]:
        print('Base \t' + str(i) + '\t' + lastDigitG(i))

if __name__ == '__main__':
    main()
