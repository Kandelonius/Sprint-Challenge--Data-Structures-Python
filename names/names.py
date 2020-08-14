import time


# from names.binary_search_tree import BSTNode
# from names.singly_linked_list import LinkedList

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the value is less than the current node's value
        if value < self.value:
            # does the current node have a left child?
            if self.left:
                self.left.insert(value)
            # otherwise, it doesn't have a left child
            # we can park the new node here
            else:
                self.left = BSTNode(value)
        # otherwise the value is greater or equal to the current node's value
        else:
            # does the current node hava a right child?
            if self.right:
                # if it does, call the right child's 'insert' method to repeat the process
                self.right.insert(value)
            # otherwise, it doesn't have a right child
            # we can park the new node here
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        # lecture
        # 1. base case
        # if the value of this node matches the target, then we've found
        # what we're looking for
        if self.value == target:
            return True
        # 2. "how do we move closer to the base case?"
        # compare the target against this node's value to determine which
        # direction we need to go in
        if target < self.value:
            # we need to go left
            # what if there is no left child?
            if not self.left:
                # then the value can't be in the tree
                return False
            # what if there is?
            else:
                # call `contains` on the left child
                return self.left.contains(target)
        else:
            # we need to go right
            # what if there is no right child?
            if not self.right:
                # then the value can't be in the tree
                return False
            # what if there is?
            else:
                # call `contains` on the right child
                return self.right.contains(target)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

initial_tree = BSTNode(names_1[0])

for name in names_1:
    if name != names_1[0]:
        initial_tree.insert(name)
for name_2 in names_2:
    if initial_tree.contains(name_2):
        duplicates.append(name_2)

# for name_2 in names_2:
#     if name_1 == name_2:
#     duplicates.append(name)


# for name in names_2:
#     if name in names_1:
#         duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
