if __name__ == '__main__':
    N = int(input())
    res = []
    for i in range(N):
        command = input().split()
        if command[0] == "append":
            res.append(int(command[1]))
        if command[0] == "remove":
            res.remove(int(command[1]))
        if command[0] == "sort":
            res.sort()
        if command[0] == "pop":
            res.pop()
        if command[0] == "reverse":
            res.reverse()
        if command[0] == "insert":
            res.insert( int(command[1]), int(command[2]) )
        if command[0] == "print":
            print(res)