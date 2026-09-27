import unittest
from app import add


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 30), 40)

if __name__ == "__main__":
    unittest.main()