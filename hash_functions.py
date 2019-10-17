import sys


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
        sys.exit(1)
        return
    elif(isinstance(N, int) is False):
        raise Exception("Error, N must be an integer")
        sys.exit(1)
        return
    elif(isinstance(key, str) is False):
        raise Exception("Error, Key must be a string")
        sys.exit(1)
        return

    key_sum = sum(map(ord, key))
    hash_to_return = key_sum % N
    return hash_to_return


def h_rolling(key, N):
    """

    """

    return None
