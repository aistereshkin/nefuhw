def is_beauty(n):
    string_repr = str(abs(n))
    digits_sum = 0
    for digit in string_repr:
        digits_sum += int(digit)
    if n % digits_sum:
        return False
    else:
        return True
print (is_beauty(1020))