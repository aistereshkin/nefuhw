n = int(input("Enter a number = "))
def is_self_dividing(n):
    get_digit_dividing = 0
    string_repr = len(str(n))
    for digit in str(n):
        if n % int(digit) == 0:
            get_digit_dividing += 1
    if get_digit_dividing == string_repr:
        return True
    else:
        return False
print(is_self_dividing(n))
