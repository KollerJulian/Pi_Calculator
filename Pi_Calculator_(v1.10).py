import decimal
import time

print("""
=========================================================================================
| 888888b.  YP                                                                          |
| 88   Y8b          Pi_Calculator by julien_Blue | inspired by DorFuchs                 |
| 88   d8P  88      v1.10    <2019>                                                     |
| 888888P'  88      Simple Pi Calculator using the Brent & Salamin algorithm for Pi     |
| 88        88      See changelog.txt for further information                           |
| 88        88                                                                          |
=========================================================================================
""")


def main():
    decimal.getcontext().prec = int(input("How many decimal places of Pi should be calculated?\nSet: ")) + 1

    try:
        d = open("pi_" + str(decimal.getcontext().prec - 1) + ".txt", "w")  # open pi.txt file
        d.write(str(pi()))  # calls pi() function and writes return value as a string to ext. file
    except PermissionError:
        import sys
        print("Failed to create or open external file... (PermissionError)")
        input("Press Enter to Exit")
        sys.exit(0)  # interrupts program if failed
    finally:
        d.close()  # close opened file to ensure it's consistence
        print("Value successfully written to external file (pi_" + str(decimal.getcontext().prec - 1) + ".txt)")
        input("Press Enter to Exit")


def pi():
    decimal.getcontext().prec += 2  # extra digits to ensure proper rounding
    decimal.getcontext().rounding = 'ROUND_DOWN'    # 'ROUND_DOWN' to ensure last digit of calculation is right
    start_time = time.time()

    # start values
    prev = 0    # 'prev' has to be unequal to 'a' to enter while loop
    a = 1
    b = 1 / decimal.Decimal(2).sqrt()
    s = 1 / decimal.Decimal(4)
    n = 0

    while(a != prev):  # recalculates value until maximum precision is reached
        prev = a
        A = (a + b) / 2 # arithmetic mean
        B = decimal.Decimal(a * b).sqrt()   # geometric mean
        S = s - 2**n * (a - A)**2   # variable s by Brent & Salamin

        # upper case letter -> n+1
        # lower case letter -> n

        # updating values for next step of calculation
        a = A
        b = B
        s = S
        n += 1

    pi = A**2/S # 'A' squared divided by 'S' equals 'pi'

    finish_time = time.time()
    decimal.getcontext().prec -= 2  # removing extra digits to write only the intended amout of decimal places to external file
    print("Done in", n + 1, "steps! (" + str(round(finish_time - start_time, 3)) + "sec)")
    return decimal.getcontext().plus(pi)    # applies the context precision and roundings to 'pi'

main()  # main function call

# end
