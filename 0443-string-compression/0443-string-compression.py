class Solution:
    def compress(self, chars: List[str]) -> int:
        left = right = index = 0
        
        while right < len(chars):
            while right < len(chars) and chars[right] == chars[left]:
                right += 1
            
            chars[index] = chars[left]
            index += 1
            
            if (right - left) > 1:
                count = str(right - left)
                for c in count:
                    chars[index] = c
                    index += 1 
                left = right
            else:
                left += 1
        
        return index
       

"""
                                 r         
    "a" "a" "b" "b" "c" "c" "c" "d"
     0   1   2   3   4   5   6   7
                                 l
        walker = runner = 0
        while runner < len(chars):
            chars[walker] = chars[runner]
            count = 1
            while runner + 1 < len(chars) and chars[runner] == chars[runner+1]:
                runner += 1
                count += 1
            if count > 1:
                for c in str(count):
                    chars[walker+1] = c
                    walker += 1
            runner += 1
            walker += 1
        return walker
"""