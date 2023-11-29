class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        res = prefix_xor = 0


        for i in range(n - 1):
            prefix_xor = arr[i]

            for k in range(i + 1, n):
                prefix_xor ^= arr[k]

                if prefix_xor == 0:
                    res  += k - i
        return res

        """
        2^3 = 1
        2^3^1 = 0

        2 3 1 6 7
        acc = 2 
        0 1 2 3 4 i
        2 3 1 6 7
            ^ 
          acc = 3^1 

        """