from typing import Optional

"""
数组实现的、固定容量的队列
"""


class ArrayQueue:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._items = [0] * capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item: int) -> bool:
        if self._tail == self._capacity:
            # 数组已满
            if self._head == 0:
                return False
            # 数据整体左移
            else:
                print("数据整体左搬移 %s 位" % self._head, end="\n")
                for i in range(0, self._tail - self._head):
                    self._items[i] = self._items[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0
        self._items.insert(self._tail, item)
        self._items[self._tail] = item
        self._tail += 1
        return True

    def dequeue(self) -> Optional[int]:
        if self._head == self._tail:
            return None
        else:
            item = self._items[self._head]
            self._head = self._head + 1
            return item

    def __repr__(self) -> str:
        return " ".join(str(item) for item in self._items[self._head: self._tail])


if __name__ == "__main__":
    q = ArrayQueue(5)
    for i in range(10):
        q.enqueue(i)
    print(q)

    for _ in range(3):
        q.dequeue()
    print(q)

    # 数据左移动
    q.enqueue(7)
    q.enqueue(8)
    print(q)
