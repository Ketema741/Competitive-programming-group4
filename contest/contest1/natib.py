N = int(input())
informations = []
for indx in range(N):
    informations.append(input().split("#"))
for info in informations:
    print(" ".join(info))