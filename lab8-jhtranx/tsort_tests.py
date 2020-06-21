import unittest
from tsort import *

class TestTsort(unittest.TestCase):

    def test_00(self):
        input = ['v1', 'v2', 'v1', 'v3', 'v2', 'v4', 'v2', 'v5', 'v1', 'v4', 'v3', 'v6', 'v5', 'v4', 'v4', 'v3', 'v4', 'v6', 'v7', 'v6', 'v4', 'v7', 'v5', 'v7']
        expect = "v1\nv2\nv5\nv4\nv7\nv3\nv6"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)   
        
    def test_01(self):
        input = ['101', '102', '102', '103', '103', '315', '225', '315', '103', '357', '315', '357', '141', '102', '102', '225']
        expect = "141\n101\n102\n225\n103\n315\n357"
        actual = tsort(input)
        # print(actual)
        self.assertEqual(actual.strip(), expect)        

    def test_02(self):
        input = ['blue', 'black', 'red', 'blue', 'red', 'green', 'green', 'blue', 'green', 'purple', 'purple', 'blue']
        expect = "red\ngreen\npurple\nblue\nblack"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_03(self):
        input = ['1', '2', '1', '9', '1', '8', '9', '8', '9', '10', '8', '11', '10', '11', '2', '3', '3', '11', '3', '4', '4', '7', '4', '5', '7', '5', '7', '13', '7', '6', '6', '14', '6', '12']
        expect = "1\n9\n10\n8\n2\n3\n4\n7\n6\n12\n14\n13\n5\n11"
        actual = tsort(input)
        # print(actual)
        self.assertEqual(actual.strip(), expect)

    def test_04(self):
        input = ['3', '8', '3', '10', '5', '11', '7', '8', '7', '11', '8', '9', '11', '2', '11', '9', '11', '10']
        expect = "7\n5\n11\n2\n3\n10\n8\n9"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_05_emptylist(self):
        input = []
        with self.assertRaises(ValueError):
            actual = tsort(input)

    def test_06_oddlist(self):
        input = ['v1']
        with self.assertRaises(ValueError):
            actual = tsort(input)
    
    def test_07_cycle(self):
        input = ['v0','v1','v1','v2','v1','v3','v3','v1']
        with self.assertRaises(ValueError):
            actual = tsort(input)

    def test_08_cycle(self):
        input = ['99','98','98','99']
        with self.assertRaises(ValueError):
            actual = tsort(input)

    def test_09_stress_hugecycle(self):
        input = ['99','98','98','97','97','96','96','95','95','94','94','93','93','99']
        with self.assertRaises(ValueError):
            actual = tsort(input)

if __name__ == "__main__":
    unittest.main()
