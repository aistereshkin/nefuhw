def get_largest_perimiter(L):
    P = 0
    n = len(L)
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                a = float(L[i])
                b = float(L[j])
                c = float(L[k])
                if b + c > a and a + c > b and a + b > c:
                    P = a + b + c
    if P == 0:
        print('False')
        return False
    else:
        print(P)
if __name__ == '__main__':
    str = input('vvedite chisla: ')
    L = str.split()
get_largest_perimiter(L)