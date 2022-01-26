class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class linked_list:
    def __init__(self, data=None):
        self.head = node(data)

    def append(self, data):
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = node(data)
        cur_node.next.previous = cur_node

    def length(self):
        count = 0
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            count += 1

        return count

    def pprint(self):
        elements = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)

        print(elements)

my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.pprint()

print(my_list.length())
