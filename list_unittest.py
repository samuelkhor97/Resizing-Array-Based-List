"""
@author: Khor Peak Siew
@since: 14/9/2018
@modified: 14/9/2018
"""

import unittest
from Resizing_Array_based_list import List


class Task2Test(unittest.TestCase):

    def test_is_empty_true(self):
        my_list = List()
        self.assertTrue(my_list.is_empty())

    def test_is_empty_false(self):
        my_list = List()
        my_list.append(1)
        self.assertFalse(my_list.is_empty())

    def test_append_empty_list(self):
        my_list = List()
        my_list.append(2)
        self.assertEqual(my_list[0], 2)

    def test_insert_valid_index_empty_list(self):
        my_list = List()
        self.assertTrue(my_list.insert(0, 1))

    def test_insert_invalid_index_empty_list(self):
        my_list = List()
        self.assertFalse(my_list.insert(1, 1))

    def test_insert_valid_index_full_list(self):
        my_list = List()
        my_list.append(1)
        self.assertTrue(my_list.insert(1, 2))

    def test_remove_valid_item(self):
        my_list = List()
        my_list.append("remove this")
        self.assertTrue(my_list.remove("remove this"))

    def test_remove_invalid_item(self):
        my_list = List()
        my_list.append(1)
        self.assertFalse(my_list.remove("remove this"))

    def test_delete_at_valid_index(self):
        my_list = List()
        for i in range(10):
            my_list.append(i)
        self.assertTrue(my_list.delete(1))

    def test_delete_at_invalid_index(self):
        my_list = List()
        for i in range(10):
            my_list.append(i)
        self.assertFalse(my_list.delete(-11))

    def test_sort_reversed(self):
        my_list = List()
        for i in range(20):
            my_list.append(i)

        comparison_list = List()
        for i in range(19, -1, -1):
            comparison_list.append(i)

        my_list.sort(True)
        self.assertEqual(my_list, comparison_list)

    def test_sort_not_reversed(self):
        my_list = List()
        for i in range(19, -1, -1):
            my_list.append(i)

        comparison_list = List()
        for i in range(20):
            comparison_list.append(i)

        my_list.sort(False)
        self.assertEqual(my_list, comparison_list)

    def test_resize_when_exceed_max_cap(self):
        my_list = List()
        for i in range(21):
            my_list.append(i)
        self.assertGreater(my_list.capacity, my_list.BASE_SIZE)

    def test_resize_when_lower_than_one_eighth_cap_used(self):
        my_list = List()
        for i in range(21):
            my_list.append(i)

        for i in range(len(my_list), my_list.capacity // 8 - 2, -1):
            my_list.delete(i)

        self.assertLessEqual(my_list.capacity, my_list.BASE_SIZE)

if __name__ == '__main__':
    unittest.main()
