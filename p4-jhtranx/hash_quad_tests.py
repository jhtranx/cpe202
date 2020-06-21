import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)
        

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)


    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)


    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])


    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)


    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)


    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)


    def test_02(self):
        ht = HashTable(5)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 2)
        ht.insert("f", 0)
        self.assertEqual(ht.get_index("f"), 3)
        ht.insert("k", 0) #causes rehash
        self.assertEqual(ht.get_index("a"), 9)
        self.assertEqual(ht.get_index("f"), 3)
        self.assertEqual(ht.get_index("k"), 8)


    def test_02b(self):
        ht = HashTable(10)
        ht.insert("drain",1)
        ht.insert("raind", 2)
        ht.insert("airdn", 3)

        self.assertEqual(ht.horner_hash("drain"), 6)

        self.assertEqual(ht.get_all_keys(), ['airdn', 'drain', 'raind'])
        self.assertEqual(ht.get_index("drain"), 6)
        self.assertEqual(ht.get_index("raind"), 7)

        self.assertEqual(ht.get_index("airdn"), 0)
        self.assertEqual(ht.get_index("asd"), None)

        ht = HashTable(10)
        ht.insert("abcx", 10000)
        ht.insert("bcdx", 30000)
        ht.insert("cdex", 50000)

        self.assertEqual(4, ht.get_index("abcx"))


    def test_insert(self):
        ht = HashTable(5)
        ht.insert("a", 0)
        ht.insert("f", 1)
        ht.insert("g", 2)
        ht.insert("k", 3)
        ht.insert("fk", 1)
        ht.insert("gk", 2)
        ht.insert("kk", 3)
        self.assertEqual(ht.in_table("gk"), True)

        #if key is already in table
        ht = HashTable(5)
        ht.insert("a", 0)
        ht.insert("a", 1)
        self.assertEqual(ht.get_value("a"), 1)


    def test_getvalue(self):
        ht = HashTable(5)
        self.assertEqual(ht.get_value("a"), None)


    def test_index(self):
        ht = HashTable(5)
        self.assertEqual(ht.get_index("a"), None)


    def test_stress(self):
        ht = HashTable(1)
        ht.insert("heaven", 'I think I can solve it')
        ht.insert("to", 'I can be your all, aint no problem baby')
        ht.insert("a", "You can be more but you’re heartless, darling, oh")
        ht.insert("tortured", "But I've already solved it")
        ht.insert("mind", "Say what you really mean, take it softer")

        self.assertEqual(ht.get_all_keys(), ['heaven', 'to', 'tortured', 'mind', 'a'])

        ht.insert("this", 0)
        ht.insert("aint", 0)
        ht.insert("by", 0) 
        ht.insert("design", 0)
        ht.insert("girl", 0)

        ht.insert("e", 0)
        ht.insert("f", 1)
        ht.insert("g", 2)
        ht.insert("k", 3)
        ht.insert("fk", 1)
        ht.insert("gk", 2)
        ht.insert("kk", 3)
        ht.insert("e", 0)
        ht.insert("f", 1)
        ht.insert("g", 2)
        self.assertEqual(ht.in_table("by"), True)
        ht.insert("k", 3)
        self.assertEqual(ht.in_table("notintable"), False)
        ht.insert("fk", 1)
        ht.insert("gk", 2)
        ht.insert("kk", 3)
        self.assertEqual(ht.in_table("gk"), True)

        self.assertAlmostEqual(ht.get_num_items(), 17)
        self.assertAlmostEqual(ht.get_table_size(), 63)
        self.assertAlmostEqual(ht.get_load_factor(), 17/63)

        #insert a bunch of cap
        ht.insert("cap", 5)
        ht.insert("cap", 5)
        ht.insert("cap", 5)
        ht.insert("cap", 5)
        ht.insert("cap", 5)
        ht.insert("cap", 5)
        ht.insert("cap", 5)
        ht.insert("cap", "nocap")

        self.assertEqual(ht.get_value("a"), "You can be more but you’re heartless, darling, oh")
        self.assertEqual(ht.get_value("mind"), "Say what you really mean, take it softer")
        self.assertEqual(ht.get_value("cap"), "nocap")
        self.assertEqual(ht.get_index("a"), 34)

        ht.insert("tacos", 5)
        ht.insert("socat", 10)
        ht.insert("tasoc", 5)
        ht.insert("asoct", 5)
        ht.insert("satoc", 5)
        ht.insert("oatsc", 5)
        ht.insert("coats", 5)
        ht.insert("tcoas", 5)
        ht.insert("tcosa", 5)
        ht.insert("scaot", 10)
        ht.insert("tasco", 5)
        ht.insert("atsoc", 5)
        ht.insert("osatc", 5)
        ht.insert("soatc", 5)
        ht.insert("scoat", 5)
        ht.insert("otcas", 5)

        self.assertEqual(ht.get_value("socat"), 10)




if __name__ == '__main__':
   unittest.main()
