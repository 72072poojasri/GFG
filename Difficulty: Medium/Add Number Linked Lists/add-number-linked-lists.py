class Solution:
    def addTwoLists(self, head1, head2):
        stack1 = []
        stack2 = []
        while head1:
            stack1.append(head1.data)
            head1 = head1.next

        # Push digits of second list
        while head2:
            stack2.append(head2.data)
            head2 = head2.next

        carry = 0
        result = None

        # Add digits
        while stack1 or stack2 or carry:
            x = stack1.pop() if stack1 else 0
            y = stack2.pop() if stack2 else 0

            total = x + y + carry
            carry = total // 10

            new_node = Node(total % 10)
            new_node.next = result
            result = new_node

        # Remove leading zeros
        while result and result.data == 0 and result.next:
            result = result.next

        return result
