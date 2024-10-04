# test_app.py
import unittest
from app import suma

class TestApp(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(suma(3, 5), 8)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
