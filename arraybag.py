'''
Name: Sonboleh Mousavi
Exercise: Chapter 5, exercise 1
Use ArrayBag to add, remove, show and clear content from an array.
'''

from ch4_ex1 import Array

class ArrayBag():
    # static variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
                # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return self.size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
            len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True

    def count(self, item):
        """Returns the number of instances of item in self."""
        total = 0
        for nextItem in self:
            if nextItem == item:
                total += 1
        return total

    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        # Exercise
        self.items[len(self)] = item
        self.size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the index of the target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        # Shift items to the left of target up by one position
        for i in range(targetIndex, len(self) - 1):
            self.items[i] = self.items[i + 1]
        # Decrement logical size
        self.size -= 1


# # Write an ArrayBag class and fill it out with 6,-1,8,5,85, -12.

# mybag = ArrayBag([6,-1,8,5,85,-12])
# mybag.add(10)
# mybag.add(20)
# print(mybag)
# #for i in range(len(mybag)):
# #   print(mybag[i])
#
# print("--------------------")
# print(mybag[0])
#
# # Check if the ArrayBag is empty.
# resp= mybag.isEmpty()
# print(f"Is arraybag empty? {resp}")
#
# # Remove the number 5 from the ArrayBag
# print("Removing element 5")
# mybag.remove(5)
#
# # print the content of the ArrayBag
# for i in mybag:
#     print(i)
#
# # In the end, make the ArrayBag empty
# mybag.clear()
#
# # Check if the ArrayBag is empty
# if mybag.isEmpty():
#     print("bag is empty")
# else:
#     print("bag is not empty")


'''
Output:
Is arraybag empty? False
Removing element 5
6
-1
8
85
-12
bag is empty
'''
