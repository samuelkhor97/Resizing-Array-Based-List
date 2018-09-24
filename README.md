# Resizing-Array-Based-List
An implementation of Resizing Array-based list that supports following operations:

• __str__(self): Returns a string representation of the list. It is structured so that there is one item
per line. Called by str(self)  
  
• __len__(self): Returns the length of the list. Called by len(self)
  
• __contains__(self, item): Returns True if item is in the list, False otherwise. Called by item in self  
  
• __getitem__(self, index): Returns the item at index in the list, if index is non-negative. If it is
negative, it will return the last item if index is −1, the second-to last if index is −2, and so on up to
minus the length of the list, which returns the first item. The function raises an IndexError if index is
out of the range from -len(self) to len(self). Called by self[index]  
  
• __setitem__(self, index, item): Sets the value at index in the list to be item. The index can be
negative, behaving as described above. Raises an IndexError if index is out of the range from
-len(self) to len(self). Called by self[index] = item  
  
• __eq__(self, other): Returns True if this list is equivalent to other. Called by self == other
  
• append(self, item): Adds item to the end of the list. The underlying array remains of fixed size. The 
operation will raise an Exception if the list is full.  
  
• insert(self, index, item): Inserts item into self before position index. The index can be negative,
behaving as described above. Raises an IndexError if index is out of the range from -len(self) to
len(self).  
  
• remove(self, item): Deletes the first instance of item from the list. Raises a ValueError if item does
not exist in self  
  
• delete(self, index): Deletes the item at index from the list, moving all items after it towards the start
of the list. The index can be negative, behaving as described above. Raises an IndexError if index is out
of the range from -len(self) to len(self).  
  
• sort(self, reverse): Sorts the items in the list in ascending order if reverse is False or descending
order if is reverse is True. Bubble Sort is implemented.  
  
• Is iterable   

• The underlying array is dynamic. The base size of the array is 20 and should never be less than 20. However, 
if the list becomes full, it is resized to be 2 times larger than the current size. Likewise, the underlying size 
should decrease by half if the underlying array is larger than the base size but the content occupies less than 1
8 of the available space. When resizing the list, contents of the list are retained. That is, when it is initially 
filled, it will be resized to 20 items, then 40, while retaining the contents initially in it. The same happens when
the size of the array shrinks.  

