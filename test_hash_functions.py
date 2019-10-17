import unittest
import random
import sys
import hash_functions as hf


class TestHashFunctions(unittest.TestCase):
    def testKeyNonString1ASCII(self):
        with self.assertRaises(Exception) as ex:
            hf.h_ascii(1, 50)
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


if __name__ == '__main__':
    unittest.main()
