class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0
        for p in patterns:
            if word.find(p) != -1:
                count += 1
        return count
