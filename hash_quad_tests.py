import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(6)
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
        ht = HashTable(7)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 6)
        ht.insert("h", 0)
        self.assertEqual(ht.get_index("h"), 0)
        ht.insert("o", 0) 
        self.assertEqual(ht.get_index("o"), 3)
        ht.insert("v", 0) # Causes rehash        
        self.assertEqual(ht.get_index("a"), 12)
        self.assertEqual(ht.get_index("h"), 2)
        self.assertEqual(ht.get_index("o"), 9)
        self.assertEqual(ht.get_index("v"), 16)

    def testsameintable(self):
        ht = HashTable(4)
        ht.insert("a", 0)
        ht.insert("a", 45)
        self.assertEqual(ht.get_value("a"), 45)

    def testrehashcollision(self):
        a = HashTable(7)
        a.insert("cat", 1)
        a.insert("tac", 45)
        a.insert("cool",2)
        a.insert("nice", 3)
        a.insert("bart", 4)
        self.assertTrue(a.in_table("cool"))
        self.assertTrue(a.in_table("nice"))
        self.assertTrue(a.get_table_size() == 17)

    def testprime1(self):
        a = HashTable(1)
        self.assertEqual(a.table_size, 2)

    def testNOne(self):
        a = HashTable(3)
        a.insert("nicee", 3)
        self.assertEqual(a.get_index("cool"), None)
        self.assertEqual(a.get_value("vat"), None)
if __name__ == '__main__':
   unittest.main()
