"""
基于链表实现栈
"""


class Node:

    def __init__(self, data: int, next=None):
        self._data = data
        self._next = next

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next


class LinkedStack:

    def __init__(self):
        self._top = None

    @property
    def top(self):
        return self._top

    def push(self, value: int):
        new_top = Node(value)
        new_top._next = self._top
        self._top = new_top

    def pop(self):
        if self._top:
            value = self._top._data
            self._top = self._top._next
            return value

    def pop_all(self):
        while self._top:
            self.pop()

    def is_empty(self):
        return not self._top

    def __repr__(self) -> str:
        current = self._top
        nums = []
        while current:
            nums.append(current._data)
            current = current._next
        return " ".join(f"{num}>" for num in nums)


if __name__ == "__main__":
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)
