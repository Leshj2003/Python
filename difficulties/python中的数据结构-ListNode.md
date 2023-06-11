## python中的数据结构-ListNode

在 Python 中，ListNode 是一种用于表示链表节点的数据结构。它通常在解决与链表相关的问题时使用。

一个 ListNode 节点包含两个主要属性：
- `val`：表示节点的值，可以是任意类型的数据。
- `next`：指向下一个节点的指针。它可以是另一个 ListNode 对象或者 None，表示链表的末尾。

通过使用多个 ListNode 节点，我们可以构建一个完整的链表结构，其中每个节点都包含一个值和指向下一个节点的指针。

以下是一个示例，展示如何使用 ListNode 构建一个简单的链表：

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 创建链表节点
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# 构建链表结构
node1.next = node2
node2.next = node3
```

在上述示例中，我们创建了三个 ListNode 节点，并通过将它们的 `next` 属性连接起来，构建了一个包含三个节点的链表：1 -> 2 -> 3。

通过操作链表的头节点，我们可以遍历整个链表，访问和修改各个节点的值，执行插入、删除等操作，以满足不同的需求。

ListNode 是解决链表相关问题的重要数据结构，在算法和数据结构领域中被广泛应用。