# from test import mode_test
if __name__ == '__main__':
    a = [9,6,5,4,1]
    N = len(a)
    print(a)
    for i in range(int(len(a) / 2)):
        a[i],a[N - i - 1] = a[N - i - 1],a[i]
    print(a)

a = [1,2,3,'b', 5]
print(a[3])