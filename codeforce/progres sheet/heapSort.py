class Solution:
    def __init__(self):
        self.heap = []

    def swap(self, heap, i, j):
        heap[i], heap[j] = heap[j], heap[i]

    def heapify_down(self, heap, n, i):
        small_child = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and heap[left] > heap[small_child]:
            small_child = left

        if right < n and arr[right] > heap[small_child]:
            small_child = right

        if small_child != i:
            self.swap(heap, i, small_child)
            self.heapify_down(heap, n, small_child)

    def buildHeap(self, heap, n):
        for i in range(n//2 - 1, -1, -1):
            self.heapify_down(heap, n, i)

    def HeapSort(self, heap, n):
        self.buildHeap(heap, n)
        for i in range(n-1, 0, -1):
            self.swap(heap, i, 0)
            self.heapify_down(heap, i, 0)

        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends