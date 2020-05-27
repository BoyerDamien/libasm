# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_ft_strlen.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dboyer <dboyer@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/27 14:33:34 by dboyer            #+#    #+#              #
#    Updated: 2020/05/27 14:39:59 by dboyer           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import unittest
import os
import random
import re
from test.utils import random_string

N_TESTS = 100

class ft_strlen(unittest.TestCase):

    def test_base(self):
        for i in range(N_TESTS):
            with self.subTest(i = i):
                string = random_string(10)
                with os.popen(f"./a.out strlen {string}") as result:
                    self.check(result)
    
    def test_empty_string(self):
        with os.popen(f'./a.out strlen \"\"') as result:
            self.check(result)
    
    def check(self, result):
        result = result.readlines()
        self.assertEqual(len(result), 2, "Wrong output format")
        result = [x.split("\t")[-1] for x in result]
        self.assertEqual(result[0], result[1], "Wrong return")