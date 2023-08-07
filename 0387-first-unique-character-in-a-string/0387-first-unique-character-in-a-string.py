class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = defaultdict(int)
        char_queue = deque()

        for i, char in enumerate(s):
            char_count[char] += 1
            char_queue.append((char, i))

            while char_queue and char_count[char_queue[0][0]] > 1:
                char_queue.popleft()

        return char_queue[0][1] if char_queue else -1