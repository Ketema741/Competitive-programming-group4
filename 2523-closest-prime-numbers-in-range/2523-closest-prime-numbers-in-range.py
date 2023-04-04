class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def prime_sieve(n):
            is_prime = [True for _ in range(n + 1)]
            is_prime[0] = is_prime[1] = False
            i = 2
            
            while i * i <= n:
                if is_prime[i]:
                    j = i * i
                    while j <= n:
                        is_prime[j] = False
                        j += i
                i += 1
                
            return is_prime
        
        primes = []
        is_prime = prime_sieve(right)
        
        for i in range(left, len(is_prime)):
            if is_prime[i]:
                primes.append(i)
                
        res = [inf, (0,0)]
        
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i-1]
            
            if diff < res[0]:
                res[0] = diff
                res[1] = (primes[i-1], primes[i])
                
        return [res[1][0], res[1][1]] if res[1][0] and res[1][1] else [-1,-1]