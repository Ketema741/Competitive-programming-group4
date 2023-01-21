class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans = []
        N = len(A)
        for indx in range(N):
            max_ = max(A[:N - indx])
            maxIndx = A.index(max_) + 1
            A[:maxIndx] = reversed(A[:maxIndx])
            ans.append(maxIndx)
            A[:N - indx] = reversed(A[:N - indx])
            ans.append(N - indx)
        return ans