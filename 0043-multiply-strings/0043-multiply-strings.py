class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = ''
        int_num_1 = 0
        int_num_2 = 0
        hash_map = {"0":0, "1":1, "2":2,"3":3, "4":4, "5":5,"6":6, "7":7, "8":8, "9":9}
        num1 = reversed(num1)
        num2 = reversed(num2)
        for indx, num in enumerate(num1):
            int_num_1 += hash_map[num]* 10**indx
            
        for indx, num in enumerate(num2):
            int_num_2 += hash_map[num]* 10**indx
       
        return str(int_num_1 * int_num_2)
        
