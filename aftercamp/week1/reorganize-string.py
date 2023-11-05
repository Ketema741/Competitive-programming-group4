class Solution:
    def reorganizeString(self, s: str) -> str:
        hash_map = Counter(s)
        maxHeap = [(-count, char) for char, count in hash_map.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            count, char = heapq.heappop(maxHeap)
            res += char
            count += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if count != 0:
                prev = (count, char)

        return res