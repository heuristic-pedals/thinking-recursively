"""Get all combinations."""


def combinations(a: list, r: int) -> int:
    """Calculate combinations.

    Given a list of size n, generate and print all possible combinations of r
    elements in the array.

    Parameters
    ----------
    a : list
        input list
    r : int
        number of combinations

    Returns
    -------
    int
        all combinations of a of length r

    """
    if r == 0:
        return [[]]  # wrap the empty list so when unpacked nothing is returned

    res = []

    for i in range(0, len(a)):
        val = a[i]
        remaining = a[i:]
        combs = combinations(remaining, r - 1)
        for comb in combs:
            res.append([val, *comb])  # unpack since returns a list

    return res


if __name__ == "__main__":
    # try some inputs
    print(combinations([1, 2, 3], r=2))
    print(combinations([".", "*", 9], r=2))
    print(combinations([1, 2], r=4))
    print(combinations([1, 2, 3], r=3))
