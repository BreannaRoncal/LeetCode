"""
Count Primes

Given an integer n, return the number of prime numbers that are strictly less than n.

 
Example 1:
  Input: n = 10
  Output: 4
  Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
  
Example 2:
  Input: n = 0
  Output: 0
  
Example 3:
  Input: n = 1
  Output: 0
 

Constraints:
  - 0 <= n <= 5 * 106


Solution is based on the Sieve of Eratosthenes

Time Complexity: O(n*log(log(n)))
Auxiliary Space: O(n)
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        prime_nums = [True for i in range(n)]
        prime_count = 0
        i = 2
        while i * i < n:
            if prime_nums[i]:
                for j in range(i*i, n, i):
                    prime_nums[j] = False
            i += 1
        
        for i in range(2, n):
            if prime_nums[i]:

                prime_count += 1
        
        return prime_count
                
