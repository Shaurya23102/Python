class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:

        def isPrime(num):
            # Prime numbers must be greater than 1
            if num <= 1:
                return False

            # Check for factors from 2 up to sqrt(num)
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        # Step 1: Count the frequency of each number
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        # Step 2: Check if any frequency is a prime number
        for value in counter.values():
            if isPrime(value):
                return True
                
        return False
