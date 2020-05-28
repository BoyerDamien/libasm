# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_ft_read.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dboyer <dboyer@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/26 16:48:07 by dboyer            #+#    #+#              #
#    Updated: 2020/05/28 14:33:14 by dboyer           ###   ########.fr        #
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
                    self.check(result, [0, string_params, len(string_params)])
    
    def test_neg_input(self):
        with self.subTest(i = 0):
            string_params = random_string(10)
            with os.popen(f"cat test_read.txt | ./a.out read 0 {string_params} -1") as result:
                self.check(result, [0, string_params, -1])
            with os.popen(f"cat test_read.txt | ./a.out read -1 {string_params} {len(string_params)}") as result:
                self.check(result, [-1, string_params, len(string_params)])
    
    def test_empty_string(self):
        string_params = random_string(10)
        with open("test_read.txt", "+w") as f:
            f.write("")
            f.write("")
        with os.popen(f"cat test_read.txt | ./a.out read 0 {string_params} {len(string_params)}") as result:
            self.check(result, [0, string_params, len(string_params)])

    def check(self, result, _input):
        result = result.readlines()
        result = [x.split(":")[1] if ":" in x else x.split("=")[1] for x in result ]
        result = [x.split("|") if "|" in x else x for x in result]
        self.assertEqual(len(result), 4, "Incorrect output format")
        self.assertEqual(result[1], result[3])
        self.assertEqual(result[0][0], result[2][0], f"Wrong output on stdout for : {_input}")
        self.assertEqual(result[0][1], result[2][1], f"Wrong return for: {_input}")
