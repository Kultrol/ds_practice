from impl_stacks import Stack
import pytest



def is_balanced_braces(s: str) -> bool:
    """
           Problem:
               Given a string, the goal is to check if the all parentheses, curly braces, and square brackets have matching open and closing pairs. That is (), {}, and [] respectively.

           Approach:
               I used a stack and hash table approach. The hash table had both open and closing braces for keys and as the values their associated open or closing braces. For example, if ")" was a key, then its associated value would be "(". This would be used for fast O(1) time lookups and comparisons.

               A for loop would iterate through each character of the string and if it was an opening brace it would push that character to the stack. If the character was a closing brace then a series of checks would occur.
                   1.) If the stack was empty, then that would indicate that there is no associated opening brace for the closing brace and return False.

                   2.) If the top element of the stack did not correspond to closing brace, then we return False.

                   3.) If, after the loop had finished, the stack was not empty, then that would indicate there remain open brace(s) with no pairing closing brace, and thus return False.
               If all of these conditions have not occurred, then we return True and conclude that all the braces/paratheses/brackets in the string have matching open and closing pairs.

               Space/Time Complexity:
               The 'brace_hash_table' has O(1)time and O(6)space complexity.

               The loop iterates through the string, so it has O(n) time traversal.

               Each append, for the worst case, we have pushes to the stack in O(1) time for O(1) space. So for a possible n appends, O(n) time and O(n) space.

               Each pop, for the worst case, we have removals in O(1) and O(1) space removals. So for a possible n pops, we have O(n) time and O(n) space

               So in total, for the worst case, this program takes O(n) time and O(n) space complexity
       """

    if len(s) == 0:
        return True

    brace_hash_table = {
        "{": "}",
        "[": "]",
        "(": ")",
        "}": "{",
        ")": "(",
        "]": "["
    }

    brace_stack:Stack = Stack()

    for char in s:
        if char == "{" or char == "[" or char == "(":
            brace_stack.push(char)

        if char == "}" or char == "]" or char == ")":
            # There is no open brace for the closing
            if len(brace_stack) == 0:
                return False

            # If the open brace/bracket doesn't match the closing one.
            if brace_hash_table[brace_stack.pop()] != char:
                return False

    if len(brace_stack) != 0:
        return False

    return True


@pytest.mark.parametrize("s, expected",[
    ("(a)", True),
    ("()", True),
    (")", False),
    ("(a}",False),
    ("{(a)", False),
    ("(a})", False)
])


def test_is_balanced_braces(s, expected):
    assert is_balanced_braces(s) == expected


