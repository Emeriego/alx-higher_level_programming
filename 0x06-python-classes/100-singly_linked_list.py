#!/usr/bin/python3
"""Task7 Defines classes for an S_list."""


class Node:
    """Class Represent a node in an S_list.
    """

    def __init__(self, data, next_node=None):
        """Initializes a new Node.
        Args:
            data (int): Data of new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = datasss
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data of Node.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next node.
        """
        return (self.__next_node)

    @next_node.setter
        """Set the next node.
        """
        return (self.__next_node)
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Class Represents an S_list.
    """

    def __init__(self):
        """Initalizes new List.
        """
        self.__head = None

    def sorted_insert(self, value):
        """Class to Insert a new Node to List.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): Node to be inserted.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            curr = self.__head
            while (curr.next_node is not None and
                    curr.next_node.data < value):
                curr = curr.next_node
            new.next_node = curr.next_node
            curr.next_node = new

    def __str__(self):
        """method Defines the print() representation
        """
        values = []
        curr = self.__head
        while curr is not None:
            values.append(str(curr.data))
            curr = curr.next_node
        return ('\n'.join(values))
