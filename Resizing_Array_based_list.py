"""
@author: Khor Peak Siew
@since: 2/9/2018
@modified: 2/9/2018
"""

from referential_array import build_array as ba


class List:

    def __init__(self):
        """
        @:self.BASE_SIZE: (int) Default capacity = 20
        @:self.capacity: (int) Current capacity
        @:self.the_array: (array) The current array
        @:self.count: (int) Current actual number of elements
        """
        self.BASE_SIZE = 20
        self.capacity = self.BASE_SIZE
        self.the_array = ba(self.capacity)
        self.count = 0

    def __str__(self):
        retval = ""
        for i in range(len(self)):
            # print every item in new line
            retval += str(self.the_array[i]) + "\n"
        return retval

    def __len__(self):
        return self.count

    def __contains__(self, item):
        # Traverse through self.the_array to look for 'item'
        for i in range(len(self)):
            if self.the_array[i] == item:
                return True
        return False

    def __getitem__(self, index):
        try:
            if index < -len(self) or index >= len(self):
                raise IndexError
            if index >= 0:
                return self.the_array[index]
                # Index '-1' for last item, '-len(self)' for first item
            elif index < 0:
                return self.the_array[index + len(self)]
        except IndexError:
            print("Index must be in between -len(self) to len(self).")

    def __setitem__(self, index, item):
        try:
            if index < -len(self) or index >= len(self):
                raise IndexError
            if index >= 0:
                self.the_array[index] = item
                # Index '-1' for last item, '-len(self)' for first item
            elif index < 0:
                self.the_array[index + len(self)] = item
        except IndexError:
            print("Index must be in between -len(self) to len(self).")

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        else:
            # Two lists are equal if both lists are of the same length
            # and every item is of same value at the same indexes
            for i in range(len(self)):
                if self.the_array[i] != other[i]:
                    return False
            return True

    def __iter__(self):
        for i in range(len(self)):
            yield self.the_array[i]

    def _resize(self, new_cap):
        """
        Helper function to resize the array to the 'new_cap' size
        """
        new_array = ba(new_cap)

        for i in range(self.count):
            new_array[i] = self.the_array[i]

        self.the_array = new_array
        self.capacity = new_cap

    def is_empty(self):
        """return True if array is empty, False if otherwise"""

        return self.count == 0

    def append(self, item):
        """
        Insert the argument 'item' passed in to end of array
        @:item: (int) Item to be appended
        """

        # resize array to 2*capacity if max capacity reached
        if self.count == self.capacity:
            self._resize(2 * self.capacity)

        # Append the item at the end of array
        self.the_array[self.count] = item
        self.count += 1

    def insert(self, index, item):
        """
        Insert the argument 'item' passed in to the 'index' passed in
        @:index: (int) Index for the item to be inserted 
        @:item: (int) Item to be inserted
        @:return: (Boolean) Return True if inserted successfully, False otherwise
        """

        # Check if -len(self) <= index <= len(self)
        valid_index = (index <= len(self)) and (index >= -len(self))

        try:
            if not valid_index:
                raise IndexError

            if self.count == self.capacity:
                self._resize(2 * self.capacity)

            # Index '-1' for last item, '-len(self)' for first item
            if index < 0:
                index = index + len(self)

            # Move every item after the 'index' to the right
            for i in range(self.count, index - 1, -1):
                self.the_array[i] = self.the_array[i - 1]

            # Insert the 'item' at 'index'
            self.the_array[index] = item
            self.count += 1

            return True

        except IndexError:
            print("Index must be in between -len(self) to len(self).")
            return False

    def remove(self, item):
        """
        Remove the argument 'item' passed in from the array if found
        @:item: (int) Item to be removed from the array
        @:return item_found: (Boolean) Return True if item found and removed successfully, False otherwise
        @complexity: Worst-Case: O(n) where n is len(self)
        @complexity: Best-Case: O(n) where n is len(self)
        """
        item_found = False

        try:
            # Traverse through the array to look for the 'item'
            for i in range(len(self)):
                if self.the_array[i] == item:
                    # Move every item after the 'item' found to left in order
                    # to remove the 'item'
                    for j in range(i, self.count - 1):
                        self.the_array[j] = self.the_array[j + 1]
                    self.count -= 1
                    item_found = True

                    if (self.capacity // 2 >= self.BASE_SIZE) and (self.count < self.capacity / 8):
                        self._resize(self.capacity // 2)
                    break

            if not item_found:
                raise ValueError

        except ValueError:
            print("Item not found in list.")

        return item_found

    def delete(self, index):
        """
        Delete the item from the array at the specified 'index'
        @:index: (int) Index of item to be removed from the array
        @:return valid_index: (Boolean) Return True if item deleted successfully, False otherwise
        @complexity: Worst-Case: O(n) where n is len(self)
        @complexity: Best-Case: O(1) 
        @precondition: There is item at 'index'
        """
        try:
            valid_index = (index < len(self)) and (index >= -len(self))
            if not valid_index:
                raise IndexError

            elif valid_index:
                if index < 0:
                    index = index + len(self)
                # Move every item after the 'index' to left
                for i in range(index, self.count - 1):
                    self.the_array[i] = self.the_array[i + 1]
                self.count -= 1

                if (self.capacity // 2 >= self.BASE_SIZE) and (self.count < self.capacity / 8):
                    self._resize(self.capacity // 2)

        except IndexError:
            print("Index must be in between -len(self) to len(self).")

        return valid_index

    def sort(self, reverse):
        """
        This function will sort elements in self.the_array, ascendingly or descendingly
        depending on the argument value of 'reverse'
        @:reverse: (Boolean) If True, sort self.the_array in descending order, False if the otherwise
        @:return: Does not return anything
        @complexity: Worst-Case: O(n^2) where n is len(self)
        @complexity: Best-Case: O(n) where n is len(self)
        @post-condition: self.the_array is sorted ascendingly/descendingly
        """

        if not reverse:
            # Traverse through all array elements
            for i in range(len(self)):

                # Last i elements are already in place
                for j in range(0, len(self) - i - 1):

                    # traverse the array from 0 to n-i-1
                    # Swap if the element found is greater
                    # than the next element
                    if self.the_array[j] > self.the_array[j + 1]:
                        self.the_array[j], self.the_array[
                            j + 1] = self.the_array[j + 1], self.the_array[j]
        else:
            # Traverse through all array elements
            for i in range(len(self)):

                # Last i elements are already in place
                for j in range(0, len(self) - i - 1):

                    # traverse the array from 0 to n-i-1
                    # Swap if the element found is less
                    # than the next element
                    if self.the_array[j] < self.the_array[j + 1]:
                        self.the_array[j], self.the_array[
                            j + 1] = self.the_array[j + 1], self.the_array[j]
