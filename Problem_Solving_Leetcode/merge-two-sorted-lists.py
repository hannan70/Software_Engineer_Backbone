class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def mergeTwoLists(list1, list2):
        head = ListNode()
        temp = head

        # Merge the two lists by comparing nodes
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        # Attach the remaining nodes (if any)
        if list1 is not None:
            temp.next = list1
        elif list2 is not None:
            temp.next = list2

        return head.next

# Helper function to create a linked list from a list
def create_linked_list(elements):
    dummy = ListNode()
    current = dummy
    for value in elements:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to display the linked list
def display_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage
list1 = create_linked_list([1, 2, 3, 4])
list2 = create_linked_list([1, 3, 4, 5, 6])


merged_head = LinkedList.mergeTwoLists(list1, list2)
display_linked_list(merged_head)
