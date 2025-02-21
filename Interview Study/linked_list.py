class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>"  % self.data

class LinkedList:
    """
    Single Linked List
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        Returns: number of nodes in the list
        Takes O(n) time.
        """
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        Adds new Node containing data at head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node or None if not found

        Takes O(n) time
        """
        current = self.head
        while current is not None:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding the node at the
        insertion point takes O(n) time.

        Takes overall O(n) time.
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            position = 0
            current = self.head
            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node or None if the key doesn't exist
        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and found is False:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current


    def remove_at_index(self, index):
        """
        Removes Node at index
        Returns the node or None if the key doesn't exist
        Takes O(n) time
        """
        current = self.head
        previous = None

        while current and index >= 0:
            if index == 0 and current is self.head:
                self.head = current.next_node
            elif index == 0:
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
            index -= 1
        return current


    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append("[%s]" % current.data)
            current = current.next_node
        return '->'.join(nodes)

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            while position < index:
                current = current.next_node
                position += 1
            return current

#
# l = LinkedList()
# l.add(1)
# l.add(2)
# l.add(3)
# l.insert(3, 2)
# print(l.size())
# print(l)
# l.remove_at_index(5)
# print(l)
# l.remove_at_index(10)
# print(l)
#
#
#
#
# print(l.search(3))
