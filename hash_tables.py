import hash_functions
import sys
import argparse


class LinearProbe:
    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N
        self.table = [None for x in range(N)]

    def add(self, key, value):
        """
        Adds an element to the hash table

        Params
        ----------
        key = key that turns into hash
        value = element that matches the key(hash)

        Return
        ----------
        True if added (errors should be caught in hash function)

        """

        totalvalues = 0
        for x in self.table:
            if x is not None:
                totalvalues = totalvalues + 1

        if totalvalues == self.N:
            raise Exception("Error, Table full")

        start_hash = self.hash_function(key, self.N)
        for i in range(self.N):
            test_slot = (start_hash + i) % self.N
            if(self.table[test_slot] is None):
                self.table[test_slot] = (key, value)
                return True

        return None

    def search(self, key):
        """
        Searches hash table for value given by key(hash)

        Parameters
        -------------
        key: key to hash, for which we will
        get its corresponding value entered earlier by
        add function

        Returns
        -------------
        None if hash-key not found in table

        Value at hash if hash-key is found
        """

        start_hash = self.hash_function(key, self.N)

        for i in range(self.N):
            test_slot = (start_hash + i) % self.N
            if(self.table[test_slot] is None):
                return None
            elif(self.table[test_slot][0] == key):
                return self.table[test_slot][1]

        pass


class ChainedHash:
    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N
        self.table = [[] for x in range(N)]

    def add(self, key, value):
        """
        Adds an element to the hash table

        Params
        ----------
        key = key that turns into hash
        value = element that matches the key(hash)

        Return
        ----------
        True if added (errors should be caught in hash function)

        """
        start_hash = self.hash_function(key, self.N)
        self.table[start_hash].append((key, value))
        return True
        pass

    def search(self, key):
        """
        Searches hash table for value given by key(hash)

        Parameters
        -------------
        key: key to hash, for which we will
        get its corresponding value entered earlier by
        add function

        Returns
        -------------
        None if hash-key not found in table

        Value at hash if hash-key is found
        """
        start_hash = self.hash_function(key, self.N)
        for i in self.table[start_hash]:
            if i[0] == key:
                return i[1]
        return None
