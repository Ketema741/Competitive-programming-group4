class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0 for _ in range(len(s) + 1)]
        s = list(s)
        for start, end, dir in shifts:
            if dir == 0:
                prefix_sum[start] -= 1
                prefix_sum[end + 1]  += 1
            else:
                prefix_sum[start] += 1
                prefix_sum[end + 1] -= 1

        running_sum = 0
        for i in range(len(s)):
            running_sum += prefix_sum[i]

            char_index = (((ord(s[i]) + running_sum) - 97) % 26) + 97

            s[i] = chr(char_index)

        return "".join(s)
            
