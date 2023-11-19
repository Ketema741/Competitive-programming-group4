from collections import defaultdict

def most_significant_bit(num):
    msb = 0
    while num != 0:
        num >>= 1
        msb += 1
    return msb

def solve():
    length = int(input())
    nums = list(map(int, input().split()))

    count = 0
    hash_map = defaultdict(int)

    for num in nums:
        msb = most_significant_bit(num)
        count += hash_map[msb]
        hash_map[msb] += 1

    return count


def main():
    test_len = int(input())
    for _ in range(test_len):
        print(solve())

main()