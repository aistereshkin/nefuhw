def number_of_matches(J, S):
    return len([1 for A in S if A in J])
if __name__ == "__main__":
    print(number_of_matches('aA', 'aAAbbbb'))
    print(number_of_matches('z', 'ZZ'))