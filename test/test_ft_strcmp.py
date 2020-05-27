# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_ft_strcmp.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dboyer <dboyer@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/27 13:16:40 by dboyer            #+#    #+#              #
#    Updated: 2020/05/27 14:47:22 by dboyer           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import unittest
import os
import random
import re
from test.utils import random_string

N_TESTS = 100

class ft_strcmp(unittest.TestCase):

    def test_base(self):
        for i in range(N_TESTS):
            with self.subTest(i = i):
                str1 = random_string(10)
                str2 = random_string(10)
                with os.popen(f"./a.out strcmp {str1} {str2}") as result:
                    self.check(result)
    
    def test_empty_string(self):
        str1 = random_string(10)
        str2 = random_string(10)
        with os.popen(f'./a.out strcmp \"\" {str2}') as result:
            self.check(result)
        with os.popen(f'./a.out strcmp {str1} \"\"') as result:
            self.check(result)

    def check(self, result):
        result = result.readlines()
        result = [x.split(":")[1] for x in result]
        result = [x.split("|") for x in result]
        self.assertEqual(len(result), 2, "Incorrect output format")
        self.assertEqual(result[0][0], result[1][0], "Wrong output on stdout")
        self.assertEqual(result[0][1], result[1][1], "Wrong return")