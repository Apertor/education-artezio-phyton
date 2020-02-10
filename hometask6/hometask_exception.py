""" home task by exception lecture"""

N = int(input("Enter number of tests: "))
STR_IN = []

if N < 10:
    for i in range(N):
        STR_IN.append(input("Test {}: input numerator and denominator: "
                            .format(i+1)))

    print("\nResult:")

    for el in STR_IN:
        numerator = el.split()[0]
        denominator = el.split()[1]

        try:
            print(int(numerator)//int(denominator))
        except ZeroDivisionError as e:
            print("Error Code: ", e)
        except ValueError as e:
            print("Error Code: ", e)
