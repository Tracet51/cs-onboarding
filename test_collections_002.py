import unittest
import collections_002


class CollectionsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test_collection = [1, 2, 3, 4, 5]
        return super().setUp()

    def test_find(self) -> None:
        test_item = 4

        index = collections_002.find(self.test_collection, test_item)

        self.assertEqual(3, index)

    def test_not_found(self) -> None:
        test_item = 7

        with self.assertRaises(ValueError):
            collections_002.find(self.test_collection, test_item)

    def test_replace(self) -> None:
        test_item = 7
        test_index = 0

        new_collection = collections_002.replace(self.test_collection, test_item, test_index)

        self.assertEqual(new_collection[test_index], test_item)
        self.assertNotEqual(id(self.test_collection), id(new_collection), "New Collection should be a copy")



    
