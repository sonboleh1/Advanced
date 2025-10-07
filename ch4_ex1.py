"""
Name: Sonboleh Mousavi
Write an Array class that has len, str, iter, getitem and setitem constructors
Then call the Array with size=6 and modify content from 3 to 8. Print array
and its size.
"""
class Array():
    """Represents an array."""
    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self.items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self.items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self.items[index] = newItem

# Create an object of this Array class with 6 elements
# my_array = Array(6)
# l = len(my_array)
# initial_value = 3
#
# # Fill the object of this class with numbers from 3 to 8.
# for i in range (l):
#     my_array[i]= initial_value + i
#
# #print the array and show the length of the array object.
# print(my_array)
# print(f"Length of the array object = {len(my_array)}")


'''
Test1:
[3, 4, 5, 6, 7, 8]
Length of the array object = 6
'''
