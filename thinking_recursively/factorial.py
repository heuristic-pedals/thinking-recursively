"""Using recursion to calculate the factorial of n."""


def factorial(n: int) -> int:
    """Calculate the factorial of n.

    Parameters
    ----------
    n : int
        input integer

    Returns
    -------
    int
        factorial of n

    """
    if n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    # check some cases
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    assert factorial(12) == 479001600
