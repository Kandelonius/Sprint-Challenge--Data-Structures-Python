class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # 1. create the Node from the value
        new_node = Node(value)
        # So, what do we do if tail is None?
        # What's the rule we want to set to indicate that the linked
        # list is empty?
        # Would it be better to check the head?
        # Let's check them both: an empty linked list has an empty
        # head and an empty tail
        if self.head is None and self.tail is None:
            # in a one-element linked list, what should head and tail
            # be referring to?
            # have both head and tail referring to the single node
            self.head = new_node
            # set the new node to be the tail
            self.tail = new_node
        else:
            # These steps assume that the tail is already referring
            # to a Node
            # 2. set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)
            # 3. reassign self.tail to refer to the new Node
            self.tail = new_node

    def remove_head(self):
        # check if the linked list empty
        if self.head is None and self.tail is None:
            return None
        # check if there is only one linked list node
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            # store the old head's value that we need to return
            val = self.head.get_value()
            # set `self.head` to the old head's `next_node`
            self.head = self.head.get_next()
            # return the old_head's value
            return val

    def remove_tail(self):
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            return None

        # check if the linked list has only one node
        if self.head == self.tail:
            # store the node we're going to remove's value
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        # otherwise, the linked list has more than one Node
        else:
            # store the last Node's value in a nother variable so we can return it
            val = self.tail.get_value()
            # we need to set `self.tail` to the second-to-last Node
            # the only way we can do this, is by traversing the whole linked list
            # from the beginning

            # starting from the head, we'll traverse down to the second-to-last Node
            # init another reference to keep track of where we are in the linked
            # list as we're iterating
            current = self.head

        # keep iterating until the node after `current` is the tail
        while current.get_next() != self.tail:
            # keep iterating
            current = current.get_next()

        # set `self.tail` to `current`
        self.tail = current
        # set the new tail's `next_node` to None
        self.tail.set_next(None)
        return val

    def contains(self, value):
        if not self.head:
            return False

        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value

# ll = Node(5)
# ll.add_to_tail(7)
# ll.add_to_tail(18)
# ll = Node(5)
# ll.set_next(Node(7))
# ll.next_node.set_next(Node(18))
# ll.next_node.next...
