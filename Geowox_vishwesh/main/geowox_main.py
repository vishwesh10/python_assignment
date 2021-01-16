def reverse_sum(num1, num2):
    """
    returns reversed sum of two reversed integers
    :param num1: first integer input
    :param num2: second integer input
    :return: integer
    """
    if not (isinstance(num1, int) and isinstance(num2, int)):
        return 0
    else:
        if num1 >= 0:
            num1 = int(str(num1)[::-1])
        else:
            num1 = int(str(abs(num1))[::-1]) * (-1)

        if num2 >= 0:
            num2 = int(str(num2)[::-1])
        else:
            num2 = int(str(abs(num2))[::-1]) * (-1)

        if num1 + num2 >= 0:
            return int(str(num1 + num2)[::-1])
        else:
            return int(str(abs(num1 + num2))[::-1]) * (-1)


if __name__ == '__main__':
    """
    If the input for number of cases is invalid than it is handed by the try-except block
    """

    try:
        no_of_cases = int(input("Enter number of cases (between 0 and 10000): "))
        if 0 < no_of_cases <= 10000:
            count = 0
            while count < no_of_cases:
                n1, n2 = map(int, input("Enter two integers separated by space ").split())
                print(reverse_sum(n1, n2))
                count = count + 1
        else:
            print(0)
    except ValueError:
        print(0)
