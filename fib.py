import argparse
import sys
from functools import cache


def fibonacci_iterative(n: int) -> int:
    """
    Computes the n-th Fibonacci number.
    :param n: n-th Fibonacci numner,
    :return: Ther m-th Fibonacci number
    """
    if n < 0:
        raise ValueError("n must be gerater than or equal to 0.")
    if n < 2:
        return n
    n0 = 0
    result1 = 0
    n1 = 1

    for i in range(n - 1):
        result1 = n0 + n1
        n0 = n1
        n1 = result1
    return result1



@cache
def fibonacci_recursive(n: int) -> int:
    """
        Computes the n-th Fibonacci number.
        :param n: n-th Fibonacci numner,
        :return: Ther m-th Fibonacci number
        """
    if n < 0:
        raise ValueError("n must be gerater than or equal to 0.")
    if n < 2:
        return n


    result1 = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

    return result1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('result1', type=int, help="Result Fibonacci number.")  # positional argument
    args = parser.parse_args()

    result = fibonacci_iterative(args.result1)
    print(result)
