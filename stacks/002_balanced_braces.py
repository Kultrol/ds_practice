from impl_stacks import Stack

def is_balanced_braces(s: str) -> bool:
    print("--------------- New Stack --------------------")
    stack = Stack()

    open_brace_table = {
        "(" : True,
        "{" : True,
        "[" : True,
    }
    closed_brace_table = {
        ")" : True,
        "]" : True,
        "}" : True,
    }

    braces_hash_table = {
        ")" : ("(",")"),
        "}" : ("{", "}"),
        "]" : ("[", "]"),
        "(": ("(", ")"),
        "{": ("{", "}"),
        "[": ("[", "]"),
    }

    for char in s:
        if open_brace_table.get(char):
            stack.push(char)

        if closed_brace_table.get(char):
            if stack.is_empty(): # Stack is empty Case -> Missing Open Brace
                print(f"Stack Empty. Missing associated open brace/bracket: '{braces_hash_table[char][0]}'")
                print("---------------- END STACK --------------------")
                print("\n")
                return False

            open_brace = stack.pop()

            if open_brace != braces_hash_table[char][0]:
                print(f"Missing Matching Pair. Got: {open_brace}, Expected: {braces_hash_table[char][0]}")
                print("---------------- END STACK --------------------")
                print("\n")
                return False

    if not stack.is_empty(): #Missing Closing Brace
        open_brace = stack.peek()
        print(f"Missing Closing Brace. "
              f"Missing associated closed brace/bracket: '{braces_hash_table[open_brace][1]}' .")
        print("---------------- END STACK --------------------")
        print("\n")
        return False

    print(f"Braces are balanced for: '{s}'") #Success Case
    print("---------------- END STACK --------------------")
    print("\n")
    return True


