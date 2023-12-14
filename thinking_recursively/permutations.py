"""Calculate permutaions of list elements."""


def permutaions(a: list, r: int) -> list:
    """Calculate permutations of list elements.

    For a list of length n, calculate the number of permutations of sample size
    r.

    Parameters
    ----------
    a : list
        input list elements
    r : int
        sample size

    Returns
    -------
    list
        permutations of elements in a using a sample size of r

    """
    if r == 0:
        return [[]]

    res = []

    for i in range(0, len(a)):
        val = a[i]
        b = a.copy()
        b.remove(val)
        rem_permutations = permutaions(b, r - 1)
        for p in rem_permutations:
            res.append([val, *p])

    return res


if __name__ == "__main__":
    # try some cases
    print(permutaions([1, 2, 3], r=2))
    print(permutaions([".", "*", 9], r=2))
    print(permutaions([1, 2], r=4))
    print(permutaions([1, 2, 3], r=3))
