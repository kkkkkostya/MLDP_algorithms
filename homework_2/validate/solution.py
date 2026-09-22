from collections.abc import Sequence


def validate_stack_sequences(pushed: Sequence[int], popped: Sequence[int]) -> bool:
    if len(pushed) != len(popped):
        return False

    stack: list[int] = []
    pop_index = 0

    for value in pushed:
        stack.append(value)

        while stack and pop_index < len(popped) and stack[-1] == popped[pop_index]:
            stack.pop()
            pop_index += 1

    return pop_index == len(popped)
