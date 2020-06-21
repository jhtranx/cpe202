import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())
    
    # # def test_03a(self):
    # #     g = Graph('test3.txt')
    # #     self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3','v4','v5','v6'], ['v7', 'v8', 'v9', 'v11']])
    # #     self.assertFalse(g.is_bipartite())

    def test_03b(self):
        g = Graph('test1.txt')
        self.assertIsNone(g.get_vertex('v99'))
        g.add_vertex('v99')
        g.add_edge('v1', 'v99')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5','v99'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v99'])

if __name__ == '__main__':
   unittest.main()
