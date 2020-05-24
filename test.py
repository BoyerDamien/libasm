import unittest
import subprocess as s

class Ft_write(unittest.TestCase):

    def test_equal(self):
        with s.Popen('./a.out write 1 damien 3', shell=True, stdout = s.PIPE) as test:
            result1 = test.stdout.readline().decode().split(":")[1]
            result2 = test.stdout.readline().decode().split(":")[1]
            print(result1, result2)
            self.assertEqual(result1, result2)
    """
    def test_notequal(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
    """

if __name__ == '__main__':
    unittest.main()