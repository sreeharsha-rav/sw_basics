def gcd(a, b):
# find gcd through simple loop
    while (b != 0):
        t = a       # set aside the value of a
        a = b       # set a equal to b
        b = t % b   # divide t (which is a) by b
    return a

if __name__ == '__main__':
    print(gcd(20, 4))   # answer should be 4 