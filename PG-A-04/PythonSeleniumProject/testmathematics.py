import unittest
from mathematics import Mathematics


class MyTestCaseU(unittest.TestCase):

    def setUp(self) -> None:
        # testlerden önce çalıştırılır
        self.math = Mathematics()

    def test_add(self):
        #self.assertEqual(True, False)  # iki değer birbirine eşit değilse tessti geçmesi
        #self.assertEqual(True, True)
        #self.assertEqual(10, 15)

        result = self.math.sumTwoNumbers(10,15)
        self.assertEqual(15, result)

    def test_multiply(self):
        self.assertEqual(5,5)

        result = self.math.multiplyTwoNumbers(10, 5)
        self.assertEqual(50, result)

    def tearDown(self) -> None:
        # testlerden sonra çalıştırılır
        pass

    if __name__ == '__main__':
        unittest.main()


