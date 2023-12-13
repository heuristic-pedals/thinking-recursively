"""Using recursion to calculate the minimum and maximum elements of a list."""


def get_min(a: list[int]) -> int:
    """Calculate the minimum of a list.

    Parameters
    ----------
    a : list
        input

    Returns
    -------
    int
        minimum element in the input

    """
    if len(a) == 1:
        return a[0]

    min_remainder = get_min(a[1:])
    return a[0] if a[0] < min_remainder else min_remainder


def get_max(a: list[int]) -> int:
    """Calculate the maximum of a list.

    Parameters
    ----------
    a : list[int]
        input

    Returns
    -------
    int
        maximum element of the input

    """
    if len(a) == 1:
        return a[0]

    max_remainder = get_max(a[1:])
    return a[0] if a[0] > max_remainder else max_remainder


if __name__ == "__main__":
    # check some test cases
    a = [6, 3, 5, 8, 0]
    assert get_min(a) == 0
    assert get_max(a) == 8

    b = [10, 329, 789, 43, 87, 87, 10]
    assert get_min(b) == 10
    assert get_max(b) == 789
