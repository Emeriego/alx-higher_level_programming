#!/usr/bin/python3
"""Task Defines classes for a S_list.
"""


class Node:
    """This Represents a node in a s_list."""

    def __init__(self, data, next_node=None):
        """This Initializes a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data of the Node.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next_node of the Node.
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This Represents a s_list.
    """

    def __init__(self):
        """This Initalizes a new S_List.
        """
        self.__head = None

    def sorted_insert(self, value):
        """This Inserts a new Node to the S_List

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): Enter the new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            t = self.__head
            while (t.next_node is not None and
                    t.next_node.data < value):
                t = t.next_node
            new.next_node = t.next_node
            t.next_node = new

    def __str__(self):
        """This Defines the print() representation of a S_List.
        """
        values = []
        t = self.__head
        while t is not None:
            values.append(str(t.data))
            t = t.next_node
        return ('\n'.join(values))
