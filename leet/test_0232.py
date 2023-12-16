import unittest
from typing import List
from dataclasses import dataclass


class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        rev_stack = []
        while self.stack:
            rev_stack.append(self.stack.pop())
        self.stack.append(x)
        while rev_stack:
            self.stack.append(rev_stack.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        print(f"peek: {queue.peek()}")
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.pop(), 1)
        self.assertFalse(queue.empty())

if __name__ == '__main__':
    unittest.main()

"""

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all
the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and
is empty operations are valid. Depending on your language, the stack may not be supported natively. You may
simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard
operations.

Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

"""
