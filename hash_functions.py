
def h_ascii(key, N):
    """
    Returns hash value based on size of array
    and sum of ASCII char values in key(string)

    Parameters
    --------------
    key: string to hash
    N: size of hash table

    Returns
    --------------
    Hash Value: index of desired element
    h_ascii(key,N) ----> element corresponding to key

    """
    if((isinstance(key, str) is False) and (isinstance(N, int) is False)):
        raise Exception("Error, Key must be a string and N must be an integer")
    elif(isinstance(N, int) is False):
        raise Exception("Error, N must be an integer")
    elif(isinstance(key, str) is False):
        raise Exception("Error, Key must be a string")
    return None


def h_rolling(key, N):
    """

    """

    return None
