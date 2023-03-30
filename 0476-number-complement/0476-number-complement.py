class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        converted ='0b'
        
        for val in binary:
            if val == '0':
                converted += '1'
            else:
                converted += '0'
                
        return int(converted, 2)
                