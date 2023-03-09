class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            smaller_char = sorted(list(s))[0]
            return s.count(smaller_char)
        
        query_list = [f(query) for query in queries]
        word_list = [f(word) for word in words]

        print(query_list, word_list)

        res = []
        for query in query_list:
            count = 0
            for word in word_list:
                if query < word:
                    count += 1
            res.append(count)
		
        return res