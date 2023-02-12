
import unittest

class OutcomesTest(unittest.TestCase):

    def player_one(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    # def test_error(self):
    #     raise RuntimeError('Test error!')

if __name__ == '__main__':
    unittest.main()
