"""Using recursion to calculate the sum from 0 to n."""


def sum_zero_to_n(n):
    """Calculate the sum of integers between 0 and n.

    Parameters
    ----------
    n : int
        integer to sum up to

    Returns
    -------
    int
        sum of integers from 0 up to n

    """
    if n == 0:  # base case - end recursion
        return 0

    return n + sum_zero_to_n(n - 1)  # recursive case


if __name__ == "__main__":
    # check some cases
    assert sum_zero_to_n(10) == 55
    assert sum_zero_to_n(100) == 5050
    assert sum_zero_to_n(500) == 125250
