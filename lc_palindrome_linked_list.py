class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        stack = []

        node = head

        while node:
            stack.append(node.val)
            node = node.next

        node = head
        while len(stack) != 0:
            actualVal = stack.pop()
            if actualVal != node.val:
                return False
            node = node.next

        return True
