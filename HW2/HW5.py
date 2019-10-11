def is_valid(braces_string):
    x = 0
    for i in range(len(braces_string)):
        if braces_string[i] == '(':
            x += 1
        else:
            x -= 1
        if x < 0:
            return False
    return x == 0
if __name__ == '__main__':
    print(is_valid("()"))
    print(is_valid("("))
    print(is_valid("()()"))
    print(is_valid("(()("))