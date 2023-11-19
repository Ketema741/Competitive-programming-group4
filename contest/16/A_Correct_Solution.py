nums = input()
shuffeled = []

for num in nums:
    shuffeled.append(num)
shuffeled.sort()

bob_answer = input()

j = 0
for i in range(len(shuffeled)):
    if int(shuffeled[i]) > 0:
        j = i
        break

shuffeled[0], shuffeled[j] = shuffeled[j], shuffeled[0]
if bob_answer == (''.join(shuffeled)):
    print("OK")
else:
    print("WRONG_ANSWER")
