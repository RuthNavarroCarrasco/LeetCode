import unittest
from solution import ListNode, Solution

class TestSumTwoNumbers(unittest.TestCase):
    
    def test_addTwoNumbers(self):
        l1 = ListNode(val=2, next= ListNode(val=4, next= ListNode(val=3)))
        l2 = ListNode(val=5, next= ListNode(val=6, next= ListNode(val=4)))
        s = Solution()
        result = s.addTwoNumbers(l1, l2)
        expected = ListNode(val=7, next=ListNode(val=0, next=ListNode(val=8)))
        self.assertEqual(result.val, expected.val)
        self.assertEqual(result.next.val, expected.next.val)
        self.assertEqual(result.next.next.val, expected.next.next.val)

if __name__ == "__main__":
    unittest.main()
