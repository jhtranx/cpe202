import unittest
import perm_lex

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])
        self.assertEqual(perm_lex.perm_gen_lex('cd'),['cd','dc'])

    def test_perm_gen_lex_02(self):
        self.assertEqual(perm_lex.perm_gen_lex('a'),['a'])

    def test_perm_gen_lex_03(self):
        self.assertEqual(perm_lex.perm_gen_lex(''),[])
    
    def test_perm_gen_lex_04(self):
        self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc','acb','bac','bca','cab','cba'])
        self.assertEqual(perm_lex.perm_gen_lex('cde'),['cde','ced','dce','dec','ecd','edc'])

if __name__ == "__main__":
        unittest.main()
