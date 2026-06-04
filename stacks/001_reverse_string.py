from impl_stacks import Stack

def reverse_string(s: str) -> str:
    s_stack: Stack = Stack()
    for char in s:
        s_stack.push(char)
    reversed_s = []

    while not s_stack.is_empty():
        reversed_s += s_stack.pop()

    return ''.join(reversed_s)
