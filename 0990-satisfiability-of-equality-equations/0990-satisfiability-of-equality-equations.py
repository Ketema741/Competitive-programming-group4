class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
    
        for equation in equations:
            a, b = equation[0], equation[-1]
            parent[a] = a
            parent[b] = b
            
        for equation in equations:
            a, sign, b = equation[0], equation[1], equation[-1]
            
            if sign == '=':
                parent_of_a = find(a)
                parent_of_b = find(b)
                
                if parent_of_a != parent_of_b:
                    parent[parent_of_a] = parent_of_b
            
            
        for equation in equations:
            a, sign, b = equation[0], equation[1], equation[-1]
            a_parent, b_parent = find(a), find(b)
            
            if sign == '!' and a_parent == b_parent:
                return False
        
        return True
            
        