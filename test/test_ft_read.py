# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_ft_read.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dboyer <dboyer@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/26 16:48:07 by dboyer            #+#    #+#              #
#    Updated: 2020/05/27 13:51:01 by dboyer           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import unittest
import os
import random
import re
from test.utils import random_string

N_TESTS = 100

class ft_read(unittest.TestCase):
    def test_base(self):
        for i in range(N_TESTS):
            with self.subTest(i = i):
                string_params = random_string(10)
                with open("test_read.txt", "+w") as f:
                    f.write(f"{string_params}")
                    f.write(f"{string_params}")
                with os.popen(f"cat test_read.txt |./a.out read 0 {string_params} {len(string_params)}") as result:
                    self.check(result)
    
    def test_neg_input(self):
        with self.subTest(i = 0):
            string_params = random_string(10)
            with os.popen(f"cat test_read.txt | ./a.out read 0 {string_params} -1") as result:
                self.check(result)
            with os.popen(f"cat test_read.txt | ./a.out read -1 {string_params} {len(string_params)}") as result:
                self.check(result)
    
    def test_empty_string(self):
        string_params = random_string(10)
        with open("test_read.txt", "+w") as f:
            f.write("")
            f.write("")
        with os.popen(f"cat test_read.txt | ./a.out read 0 {string_params} {len(string_params)}") as result:
            self.check(result)

    def check(self, result):
        result = result.readlines()
        result = [x.split(":")[1] for x in result]
        result = [x.split("|") for x in result]
        self.assertEqual(len(result), 2, "Incorrect output format")
        self.assertEqual(result[0][0], result[1][0], "Wrong output on stdout")
        self.assertEqual(result[0][1], result[1][1], "Wrong return")
