import unittest
import random
import sys
import hash_functions as hf
from hash_tables import LinearProbe
from hash_tables import ChainedHash


class TestHashTables(unittest.TestCase):
    def testLinearProbeAddFull(self):
        test_obj = LinearProbe(10, hf.h_ascii)
        for i in range(0, 10):
            test_obj.add(("a" + str(i)), 1 + i)

        with self.assertRaises(Exception) as ex:
            test_obj.add("a0", 1)
        output = str(ex.exception)
        self.assertEqual(output, "Error, Table full")

    def testLinearProbeAddWorking(self):
        test_obj = LinearProbe(10, hf.h_ascii)
        for i in range(0, 9):
            test_obj.add(("a" + str(i)), 1 + i)

        self.assertEqual(True, test_obj.add("a0", 1))

    def testLinearProbeSearch(self):
        test_obj = LinearProbe(10, hf.h_ascii)
        for i in range(0, 10):
            test_obj.add(("a" + str(i)), 1 + i)

        self.assertEqual(1, test_obj.search("a0"))

    def testChainedHash(self):
        test_obj = ChainedHash(10, hf.h_ascii)
        for i in range(0, 10):
            test_obj.add("a" + str(i), 1 + i)
        self.assertEqual(True, test_obj.add("a0", 1))

    def testChainedHashSearchChain(self):
        test_obj = ChainedHash(10, hf.h_ascii)
        test_obj.add("a", 1)
        test_obj.add("k", "return this, not 1")
        self.assertEqual("return this, not 1", test_obj.search("k"))


if __name__ == '__main__':
    unittest.main()
