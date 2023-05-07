# Linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.__dict__}'


class LinkedList:
    def __init__(self):
        # self._head = None
        self._head = None

    def __add__(self, other):
        l = LinkedList()
        l.head = self.head
        length = len(l)
        l[length - 1].next = other.head
        return l

    def __repr__(self):
        return f'{self.__dict__}'

    def __len__(self):
        count = 0
        next_node = self.head
        while next_node != None:
            count += 1
            next_node = next_node.next
        return count

    #   Works for getting the item at [i]
    #
    def __getitem__(self, key):
        count = 0
        next_node = self.head
        while next_node != None:
            if count == key:
                return next_node
            next_node = next_node.next
            count += 1

    def __mul__(self, value):
        last_node = self[len(self) - 1]
        next_node = self.head
        for x in range(value):
            while next_node != None:
                last_node.next = next_node
                # last_node = self[len(self) - 1]
                next_node = next_node.next
                print(next_node.next)
        return next_node

    # TODO
    # for slicing
    # def __getitem__(self, start, stop, step):
    #     count = 0
    #     nextNode = self.head
    #     while nextNode != None:
    #         if count == key:
    #             return nextNode
    #         nextNode = nextNode.next
    #         count += 1

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        if type(value) == Node:
            self._head = value
        else:
            raise TypeError('Has to be a Node type')


def Main():
    llist = LinkedList()
    # head is a pointer to a Node with data off 'Data of First Node'
    llist.head = Node('1st Node')
    llist.head.next = Node('2nd Node')  # next belongs to 'Data
    llist.head.next.next = Node('3rd node')
    llist.head.next.next.next = Node('4th node')
    llist.head.next.next.next.next = Node('5th node')

    newlinked = LinkedList()
    newlinked.head = Node('a')
    newlinked.head.next = Node('b')

    # print(len(llist))

    # print(llist[4].data)

    # llist + newlinked
    # print(llist)

    new = llist * 2
    # print(len(new))


Main()
