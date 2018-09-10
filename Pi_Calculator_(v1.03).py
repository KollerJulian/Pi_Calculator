import decimal
import time
import sys

print("""
=============================================================================
| 888888b.  YP                                                              |
| 88   Y8b          Pi_Calculator by julien_Blue                            |
| 88   d8P  88      v1.03   <2018>                                          |
| 888888P'  88      Simple Pi Calculator using the Chudnovsky Algorithm     |
| 88        88      See README.md for further information                   |
| 88        88                                                              |
=============================================================================
""")


def main():
    decimal.getcontext().prec = int(input("How many decimal places of Pi should be calculated?\nSet: ")) + 1

    try:
        d = open("pi.txt", "w")  # open pi.txt file
    except PermissionError:
        input("Failed to create or open external file... (PermissionError)\nPress Enter to Exit")
        sys.exit(0)  # interrupts program if failed

    d.write(str(pi()))  # calls pi() function and writes return value as a string to ext. file
    d.close()  # close opened file to ensure it's consistence
    print("Value successfully written to external file (pi.txt)")
    input("Press Enter to Exit")


def pi():  # Chudnovsky Algorithm
    start_time = time.time()
    decimal.getcontext().prec += 2  # extra digits for intermediate steps
    three = decimal.Decimal(3)  # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    print("Calculating...")

    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t

    decimal.getcontext().prec -= 2
    finish_time = time.time()
    print("Done", '(' + str(round(finish_time - start_time, 3)) + 's)!')
    return +s


main()  # calls the main function

# end
