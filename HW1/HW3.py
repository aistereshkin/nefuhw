n = int(input("Enter a number = "))
def is_power_of_two(n):
    while n > 1:
        n /= 2
    if n == 1:
        return (True)
    else:
        return (False)
print (is_power_of_two(n))
