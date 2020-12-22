
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkList:

    def __init__(self):
        self.head = ListNode(0)
    
        current = self.head

        for i in range(1,10):
            node = ListNode(i)
            current.next = node
            current = node

    def printList(self):
        current = self.head

        my_list = []
        while current:
            my_list.append(current.val)
            current = current.next

        print(f'{my_list}')

    def reverseList(self):

        new_head = None
        current = self.head
        next = current.next        

        while current is not None:
            current.next = new_head
            new_head = current
            current = next
            if next is not None:
                next = next.next

        self.head = new_head

def main():

    LL = LinkList()

    LL.printList()
    LL.reverseList()
    LL.printList()


if __name__ == '__main__':
    main()