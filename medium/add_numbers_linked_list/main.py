from random import randint
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number_list1 = int(''.join(map(str, [node.val for node in l1])))
        number_list2 = int(''.join(map(str, [node.val for node in l2])))
        sum = number_list1 + number_list2 
        print(f"The sum is {sum}")
        return self.create_linked_list_from_number(self, result=sum)

    def create_linked_list_from_number(self, result: int):
        
        # Convert the number into a string so it's easier to manipulate
        num_str = str(result)[::-1]
        # Omit leading zeros if present
        while num_str.startswith("0"):
            num_str = num_str[1:]
            
        # Create an empty list to store the nodes
        nodes = []
        for digit in num_str:
            node = ListNode(int(digit))
            nodes.append(node)
        
        # Connect the nodes in the list
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        
        # Return the head of the list
        return nodes


# def build_linked_list(length):
        
#         head_val = 0
#         while head_val == 0:
#             head_val = randint(1, 9)
#         nodes = [ListNode(randint(0, 9)) for _ in range(length)]
#         for i in range(length - 1):
#             nodes[i].next = nodes[i + 1]
#         return nodes
    
# linked_list1 = build_linked_list(3)
# linked_list2 = build_linked_list(4)
# print("FIRST LINKED LIST")
# for node in linked_list1:
    
#     print(node.val)

# print("SECOND LINKED LIST")
# for node in linked_list2:
    
#     print(node.val)
# # print("Con valores") if linked_list1 else print("Sin valores")
# res = Solution.addTwoNumbers(Solution, linked_list1, linked_list2)

# for node in res:
    
#     print(node.val)

