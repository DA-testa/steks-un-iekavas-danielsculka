# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if not len(opening_brackets_stack):
                return i

            last_opening_bracket = opening_brackets_stack[len(opening_brackets_stack) - 1]

            if are_matching(last_opening_bracket[0], next):
                opening_brackets_stack.remove(last_opening_bracket)
            else:
                return i
                
            pass
    
    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0][1]

    return -1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == -1:
        print("Success")
    else:
        print(mismatch + 1)


if __name__ == "__main__":
    main()
