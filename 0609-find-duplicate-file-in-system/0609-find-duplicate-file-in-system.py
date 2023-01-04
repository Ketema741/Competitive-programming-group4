class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hash_map = collections.defaultdict(list)
        for line in paths:
            data = line.split()
            root = data[0]
            for file in data[1:]:
                name, x, content = file.partition('(')
                hash_map[content[:-1]].append(root + '/' + name)        
        return [x for x in hash_map.values() if len(x) > 1]
            