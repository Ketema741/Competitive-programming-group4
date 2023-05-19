class Solution:
    def __init__(self):
        self.representative = [i for i in range(26)]

    def find(self, x):
        if self.representative[x] == x:
            return x
        self.representative[x] = self.find(self.representative[x])
        return self.representative[x]

    def performUnion(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if x < y:
            self.representative[y] = x
        else:
            self.representative[x] = y

    def smallestEquivalentString(self, s1, s2, baseStr):

        for i in range(len(s1)):
            self.performUnion(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))

        res = ""
        for char in baseStr:
            res += chr(self.find(ord(char) - ord('a')) + ord('a'))

        return res
