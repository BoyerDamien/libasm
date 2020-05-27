# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_ft_strcpy.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dboyer <dboyer@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/27 14:15:53 by dboyer            #+#    #+#              #
#    Updated: 2020/05/27 14:31:49 by dboyer           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import unittest
import os
import random
import re
from test.utils import random_string


N_TESTS = 100

class ft_strcpy(unittest.TestCase):

    def test_base(self):
        for i in range(N_TESTS):
            with self.subTest(i = i):
                src = random_string(10)
                dest = "".join(["0" for _ in range(len(src))])
                with os.popen(f"./a.out strcpy {dest} {src}") as result:
                    self.check(result)
    
    def test_empty_string(self):
         with os.popen(f'./a.out strcpy test \"\"') as result:
            self.check(result)
    

    def check(self, result):
        result = result.readlines()
        self.assertEqual(len(result), 4, "Wrong output format")
        result = [x.split("|")[1] for x in result if len(x.split("|")) > 1]
        self.assertEqual(result[0], result[1], "Wrong return value")
        self.assertEqual(result[2], result[3], "Wrong copied value")