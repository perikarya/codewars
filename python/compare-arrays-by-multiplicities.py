def comp(array1, array2):
    try:
        return sorted(array2) == sorted([i * i for i in array1])
    except TypeError:
        return False
