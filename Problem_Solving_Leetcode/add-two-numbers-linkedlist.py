
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        temp = dummy
        carry = 0
        while l1 or l2 or carry:

            # get value from the current node if value present otherwise 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # calculate sum and carry
            sum = val1 + val2 + carry
            carry = sum // 10
            digit = sum % 10

            temp.next = ListNode(digit)
            temp = temp.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next


        return dummy.next


    # create linked list from array/list
    @staticmethod
    def create_linked_list(data):
        head = ListNode(data[0])
        current = head
        for value in data[1:]:
            current.next = ListNode(value)
            current = current.next
        return head


    # Display the linked list
    @staticmethod
    def display_linked_list(result_head):
        current = result_head
        while current:
            print(current.val, end=' -> ')
            current = current.next
        print("None")



list1 = LinkedList.create_linked_list([2, 4, 3])
list2 = LinkedList.create_linked_list([5, 6, 4])
ll = LinkedList()
result_head = ll.addTwoNumbers(list1, list2)
ll.display_linked_list(result_head)
