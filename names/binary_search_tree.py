"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


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

    # Return True if the tree contains the value
    # False if it does not
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

    """
    #my work
        # midpoint = 0
        if self.value == target:
            return True
        elif self.right is None and self.left is None:
            return False
        # assuming the data set is sorted check if left is smaller than the target
        elif self.value > target:
            # print(f"right is {self.right.value} left is {self.left.value}")
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        elif self.value < target:
            # print(f"left is {self.left.value} right is {self.right.value}")
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
    """

    # Return the maximum value found in the tree
    def get_max(self):
        # Lecture start
        # #recursive
        # if not self.right:
        #     return self.value
        # return self.right.get_max()

        # iterative
        current = self
        while current.right:
            current = current.right
        return current.value
        # Lecture end
        # # self.left will always be smaller than self.right so max will always be to the right.
        # # if self.left is not None:
        # #     if self.left.value > self.value:
        # #         return self.left.get_max()
        # #     else:
        # #         return self.value
        # # print(f"self.right is {self.right} self.value is {self.value}")
        # if self.right is not None:
        #     # print(f"self.right.value is {self.right.value} self.value is {self.value}")
        #     if self.right.value > self.value:
        #         return self.right.get_max()
        #     else:
        #         return self.value
        # else:
        #     return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # lecture start
        # #Recursive
        # #call fn on self.value
        # fn(self.value)
        # #check if self has a left child
        # if self.left:
        #     #call 'for_each' on the left child, passing fn on that child
        #     self.left.for_each(fn)
        # #check if self has a right child
        # if self.right:
        #     # call 'for_each' on the right child, passing fn on that child
        #     self.right.for_each(fn)
        # #depth first(LIFO) iterative
        # stack = []
        # #add the root node to our stack
        # stack.append(self)
        # while len(stack) > 0:
        #     current_node = stack.pop()
        #     if current_node.right:
        #         stack.append(current_node.right)
        #     if current_node.left:
        #         stack.append(current_node.left)
        #     fn(current_node.value)
        # bredth first(FIFO) traversal
        from collections import deque
        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            fn(current_node.value)
        # lecture end
        #
        # fn(self.value)
        # if self.left is not None:
        #     self.left.for_each(fn)
        # if self.right is not None:
        #     # fn(self.value)
        #     self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # bring in a queue
        from collections import deque
        q = deque()
        q.append(self)

        while (len(q) > 0):
            current = q.popleft()
            print(current.value)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            # print(current)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = []
        # add the root
        stack.append(self)
        while len(stack) > 0:
            # remove current from the stack
            current = stack.pop()
            if current.right:
                # add right to the stack
                stack.append(current.right)
            if current.left:
                # add left to the stack
                stack.append(current.left)
            print(current.value)
        # #recursive
        # print(self.value)
        # if self.left:
        #     self.left.dft_print()
        # if self.right:
        #     self.right.dft_print()

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # 1. Visit root node
    # 2. Visit all the nodes in the left subtree
    # 3. Visit all the nodes in the right subtree
    def pre_order_dft(self, root):
        res = []
        if root:
            res.append(root.value)
            print(root.value)
            if root.left:
                res = res + self.pre_order_dft(root.left)
            if root.right:
                res = res + self.pre_order_dft(root.right)
        return res

    # Print Post-order recursive DFT
    # 1. Visit all the nodes in the left subtree
    # 2. Visit all the nodes in the right subtree
    # 3. Visit the root node.
    def post_order_dft(self, root):
        res = []
        if root:
            if root.left:
                res = self.post_order_dft(root.left)
            if root.right:
                res = res + self.post_order_dft(root.right)
            res.append(root.value)
            print(root.value)
        return res


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
# bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
# bst.post_order_print()
