#User function Template for python3

class Solution: 
   
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min = i
            for j in range(i+1, n):
                if arr[min] > arr[j]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
