


def main():
    n = int(input)
    nums = list(map(int, input().split()))
    res = [0]*n
    res[0] = 1
    for i in range(4,n+1,2):
        res[i] = 2

    for i in range(3, n+1,2):
        res[i] = 1

main()