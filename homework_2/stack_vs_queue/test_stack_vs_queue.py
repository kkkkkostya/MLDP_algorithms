import pytest

from .solution import Queue, Stack


def test_stack_has_lifo_order() -> None:
    stack = Stack[int]()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert len(stack) == 3
    assert stack.peek() == 30
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.is_empty()


def test_queue_has_fifo_order_and_can_be_reused() -> None:
    queue = Queue[str]()
    queue.enqueue("first")
    queue.enqueue("second")
    queue.enqueue("third")

    assert len(queue) == 3
    assert queue.peek() == "first"
    assert queue.dequeue() == "first"
    assert queue.dequeue() == "second"
    assert queue.dequeue() == "third"
    assert queue.is_empty()

    queue.enqueue("new")
    assert queue.peek() == "new"
    assert queue.dequeue() == "new"


@pytest.mark.parametrize("container", [Stack(), Queue()])
def test_empty_container_operations_raise_index_error(container: Stack | Queue) -> None:
    with pytest.raises(IndexError):
        container.peek()

    with pytest.raises(IndexError):
        if isinstance(container, Stack):
            container.pop()
        else:
            container.dequeue()
