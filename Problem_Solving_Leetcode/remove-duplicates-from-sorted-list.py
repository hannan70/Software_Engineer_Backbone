
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def remove_duplicate(self):
        current = self.head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return self.head


    def display_linked_list(self):
        current = self.head
        while current:
            print(current.val, end=' -> ')
            current = current.next
        print("None")


head = ListNode(1, ListNode(1, ListNode(5, ListNode(7))))

ll =  LinkedList(head)
ll.mergeTwoLists()
ll.display_linked_list()
