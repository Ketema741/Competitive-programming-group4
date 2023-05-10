class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for recipe, ingredient in zip(recipes, ingredients):
            indegree[recipe] = len(ingredient)
            
            for ingre in ingredient:
                graph[ingre].append(recipe)
        
        res = []
        queue = deque(supplies)
        recipes = set(recipes)
        
        while queue:
            supply = queue.popleft()
            
            if supply in recipes:
                res.append(supply)
            for recipe in graph[supply]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    queue.append(recipe)
        return res