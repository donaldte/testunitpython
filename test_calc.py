import unittest 
import app 



class TestCalc(unittest.TestCase):

    def test_add(self) -> None:
        result = app.add(10, 5)
        self.assertEqual(result, 15)
 
    
    def test_sub(self) -> None:
        result = app.substract(10, 5)
        self.assertEqual(result, 5)

    
    def test_mul(self) -> None:
        result = app.multiply(10, 5)
        self.assertEqual(result, 50)

    
    def test_div(self) -> None:
        result1 = app.divide(10, 5)
        result2 = app.divide(5, 2)
        self.assertEqual(result1, 2)
        self.assertEqual(result2, 2.5)


        # self.assertRaises(ValueError, app.divide, 10, 0)

        with self.assertRaises(ValueError):
            app.divide(10, 0)


















if __name__ == '__main__':
    unittest.main()
