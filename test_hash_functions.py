import unittest
import random
import sys
import hash_functions as hf


class TestHashFunctions(unittest.TestCase):
    def testKeyNonString1ASCII(self):
        with self.assertRaises(Exception) as ex:
            hf.h_ascii(12, 50)
        output = str(ex.exception)
        self.assertEqual(output, "Error, Key must be a string")

    def testKeyNonString2ASCII(self):
        testlist = [1, 2, 3]
        with self.assertRaises(Exception) as ex:
            hf.h_ascii(testlist, 50)
        output = str(ex.exception)
        self.assertEqual(output, "Error, Key must be a string")

    def testNnonInteger1(self):
        with self.assertRaises(Exception) as ex:
            hf.h_ascii("KeyIsString", "this should not be a string")
        output = str(ex.exception)
        self.assertEqual(output, "Error, N must be an integer")

    def testNnonInteger2(self):
        testlist = [1, 2, 3]
        with self.assertRaises(Exception) as ex:
            hf.h_ascii("KeyIsString", testlist)
        output = str(ex.exception)
        self.assertEqual(output, "Error, N must be an integer")

    def testBothWrongInputsASCII(self):
        ermsg = "Error, Key must be a string and N must be an integer"
        with self.assertRaises(Exception) as ex:
            hf.h_ascii(123, "wrong input")
        output = str(ex.exception)
        self.assertEqual(output, ermsg)

    def testASCIIsum(self):
        testkey = "abc"
        testkey_ASCII_sum = 294
        table_size = 290
        expected_return_val = 4
        self.assertEqual(expected_return_val, hf.h_ascii(testkey, table_size))

    def testRollingKey1(self):
        with self.assertRaises(Exception) as ex:
            hf.h_rolling(12, 50)
        output = str(ex.exception)
        self.assertEqual(output, "Error, Key must be a string")

    def testRollingKey2(self):
        testlist = [1, 2, 3]
        with self.assertRaises(Exception) as ex:
            hf.h_rolling(testlist, 50)
        output = str(ex.exception)
        self.assertEqual(output, "Error, Key must be a string")

    def testRollingN1(self):
        with self.assertRaises(Exception) as ex:
            hf.h_rolling("KeyIsString", "this should not be a string")
        output = str(ex.exception)
        self.assertEqual(output, "Error, N must be an integer")

    def testRollingN2(self):
        testlist = [1, 2, 3]
        with self.assertRaises(Exception) as ex:
            hf.h_rolling("KeyIsString", testlist)
        output = str(ex.exception)
        self.assertEqual(output, "Error, N must be an integer")

    def testBothWrongInputsRolling(self):
        ermsg = "Error, Key must be a string and N must be an integer"
        with self.assertRaises(Exception) as ex:
            hf.h_rolling(123, "wrong input")
        output = str(ex.exception)
        self.assertEqual(output, ermsg)

    def testRollingHashOutput(self):
        testkey = "abc"
        akI = [97, 98, 99]
        p = 53
        m = 2**64
        n = 100
        sum_test = 0
        for i in range(0, 3):
            sum_test += akI[i] * p**i
        sum_test = sum_test % m
        self.assertEqual(sum_test % n, hf.h_rolling(testkey, n))


if __name__ == '__main__':
    unittest.main()
