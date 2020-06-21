# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
    
    def test_postfix_eval_DivideByZero(self):
        try:
            postfix_eval('1 0 /')
            self.fail()
        except ValueError as e:
            pass
        try:
            postfix_eval('1 1 + 0 /')
            self.fail()
        except ValueError as e:
            pass
        
    def test_postfix_eval_BitshiftError(self):
        try:
            postfix_eval('1 1.0 >>')
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

        try:
            postfix_eval('1 1.0 <<')
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_floats(self):
        self.assertAlmostEqual(postfix_eval("3 5.5 +"), 8.5)
        self.assertAlmostEqual(postfix_eval("5.5 3 +"), 8.5)
    
    def test_postfix_eval__negative_and_floats(self):
        self.assertAlmostEqual(postfix_eval("-4.0 4.0 +"), 0)
        self.assertAlmostEqual(postfix_eval("-3.0 1.0 -"), -4.0)
        self.assertAlmostEqual(postfix_eval("6.0 -9.0 *"), -54.0)
        self.assertAlmostEqual(postfix_eval("10.0 -1.0 /"), -10.0)
        self.assertAlmostEqual(postfix_eval("-2.0 4.0 **"), 16.0)
        
    def test_postfix_eval_operators(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
        self.assertAlmostEqual(postfix_eval("3 5 -"), -2)
        self.assertAlmostEqual(postfix_eval("3 5 *"), 15)
        self.assertAlmostEqual(postfix_eval("4 2 /"), 2)
        self.assertAlmostEqual(postfix_eval("4 2 **"), 16)
        self.assertAlmostEqual(postfix_eval("20 1 >>"), 10)
        self.assertAlmostEqual(postfix_eval("20 1 <<"), 40)
    
    def test_postfix_eval_stress(self):
        self.assertAlmostEqual(postfix_eval("5 1 2 + 4 ** + 3 -"), 83)
        self.assertAlmostEqual(postfix_eval("6 4 3 + 2 - * 6 /"), 5)
        self.assertAlmostEqual(postfix_eval("5 2 4 * + 7 2 - 4 6 2 / 2 - * + 4 - +"), 18)
        self.assertAlmostEqual(postfix_eval("5 2 4 * + 7 2 - 4 6 2 / 2 - * + 4 - + 6 4 3 + 2 - * 6 / - 5 1 2 + 4 ** + 3 - +"), 96)

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
    
    def test_infix_to_postfix_precedence(self):
        self.assertEqual(infix_to_postfix('3 << 4'), '3 4 <<')
        self.assertEqual(infix_to_postfix('15 - 4 * 3'), '15 4 3 * -')
        self.assertEqual(infix_to_postfix('6 << 7 << 8'), '6 7 << 8 <<')
        self.assertEqual(infix_to_postfix('2 >> 3 ** 4'), '2 3 >> 4 **')
        self.assertEqual(infix_to_postfix('3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3'), '3 4 2 * 1 5 - 2 3 ** ** / +')
        self.assertEqual(infix_to_postfix('3 - 7 * 3 + 2'), '3 7 3 * - 2 +')
        self.assertEqual("5 6 3 + 7 3 * - 2 + * 6 /", infix_to_postfix("5 * ( 6 + 3 - 7 * 3 + 2 ) / 6"))

    def test_infix_to_postfix_stress(self):
        self.assertEqual("3 4 2 * 1 5 - 2 3 5 ** ** / 6 3 + 7 3 * - 2 + * 6 / +", infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3 5 * ( 6 + 3 - 7 * 3 + 2 ) / 6"))

        
    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_prefix_to_postfix_1(self):
        self.assertEqual(prefix_to_postfix('** -100 2'), '-100 2 **')
        self.assertEqual(prefix_to_postfix('+ << 99 98 >> 97 96'), '99 98 << 97 96 >> +')
    
    def test_prefix_to_postfix_stress(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

if __name__ == "__main__":
    unittest.main()
