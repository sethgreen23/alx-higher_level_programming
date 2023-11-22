#!/usr/bin/python3
"""Module Node"""


class Node:
    """
    Node class that define singly linked list.

    Artributes:
        data (int): data of the Node.
        next_node (Node): next node of the Node.
    """
    def __init__(self, data, next_node=None):
        """
        Initilize a Node Object.
        Parametes:
            data (int): data of the Node
            next_node (Node): next_node of the Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Define data"""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Define the value of data
        Parameters:
            value (int): attribute to assingn to data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Define next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Define the value to the next_node
        Parameters:
            value (Node): attribute to assign to node
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Singly linked list class that define singly linked list.

    Artributes:
        head (Node): data of the Node.
    """
    def __init__(self):
        """
        Initilize a Singly linked list Object.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a node in a sorted Increasing Linked list
        Parameters:
            value (int): value to insert
        """
        new_node = Node(value, None)
        if self.__head is None:
            self.__head = new_node
        else:
            prev = None
            temp = self.__head
            while temp is not None and temp.data < value:
                prev = temp
                temp = temp.next_node
            if prev is None:
                if self.__head.data > value:
                    new_node.next_node = self.__head
                    self.__head = new_node
                else:
                    self.__head.next_node = new_node
            elif temp is None:
                prev.next_node = new_node
            else:
                new_node.next_node = temp
                prev.next_node = new_node

    def __str__(self):
        """Redefinition of str function"""
        temp = self.__head
        str_ret = ""
        while temp is not None:
            str_ret += str(temp.data)+"\n"
            temp = temp.next_node
        return str_ret
