# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_ft_write.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dboyer <dboyer@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/26 16:29:45 by dboyer            #+#    #+#              #
#    Updated: 2020/05/28 14:30:00 by dboyer           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import unittest
import os
import random
import re
import subprocess
from test.utils import random_string

N_TESTS = 100

class ft_write(unittest.TestCase):
    def test_base(self):
        for i in range(N_TESTS):
            with self.subTest(i = i):
                string_params = random_string(10)
                with os.popen(f"./a.out write 1 {string_params} {len(string_params)}") as result:
                    self.check(result, [1, string_params, len(string_params)])
    
    def test_random_size(self):
        for i in range(N_TESTS):
            with self.subTest(i = i):
                string_params = random_string(10)
                size = random.randint(-20, 20)
                with os.popen(f"./a.out write 1 {string_params} {size}") as result:
                    self.check(result, [1, string_params, size])
    
    def test_fd(self):
        for i in range(5):
            with self.subTest(i = i):
                string_params = random_string(10)
                fd = -1 + i
                with os.popen(f"./a.out write {fd} {string_params} {len(string_params)}") as result:
                    self.check(result, [fd, string_params, len(string_params)])
                if fd == 3:
                    with open("./test_write.txt", "+r") as f:
                        content = f.read()
                        exp = rf"{string_params}"
                        result = re.findall(exp, content)
                        self.assertEqual(len(result), 2, f"ft_write does not write on fd {fd}")
                        self.assertEqual(result[0], result[1])
    
    def test_empty_string(self):
        for i in range(10):
            with self.subTest(i = i):
                size = random.randint(-10, 10)
                with os.popen(f"./a.out write 1 \'\' {size}") as result:
                    self.check(result, [1, "", size])

    def check(self, result, _input):
        result = result.readlines()
        result = [x.split(":")[1] if ":" in x else x.split("=")[1] for x in result ]
        result = [x.split("|") if "|" in x else x for x in result]
        self.assertEqual(len(result), 4, "Incorrect output format")
        self.assertEqual(result[1], result[3])
        self.assertEqual(result[0][0], result[2][0], f"Wrong output on stdout for : {_input}")
        self.assertEqual(result[0][1], result[2][1], f"Wrong return for: {_input}")