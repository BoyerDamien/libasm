import unittest
import os
import random
import re
from test.utils import random_string

N_TESTS = 100

class ft_strdup(unittest.TestCase):

    def test_base(self):
        for i in range(N_TESTS):
            with self.subTest(i = i):
                string = random_string(10)
                with os.popen(f"./a.out strdup {string}") as result:
                    self.check(result)
    
    def test_empty_string(self):
        with os.popen(f'./a.out strdup \"\"') as result:
            self.check(result)
    
    def check(self, result):
        result = result.readlines()
        result = [x.split(":")[-1] for x in result]
        self.assertEqual(len(result), 3, "Incorrect output format")
        self.assertEqual(result[0], result[1], "Wrong output on stdout")
        self.assertNotEqual(result[1], result[2], "The string was not duplicated")