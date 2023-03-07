testCase = int(input())

for _ in range(testCase):
    w, et, ef = map(int, input().split())
    
    zeroToFour = et * 4
    curntToFour = (4 - ef) * et
    curntToZero = zeroToFour - curntToFour
    walk = w*ef
    
    minTime = min((w*4, walk + curntToFour, curntToZero + zeroToFour))
    print(minTime)