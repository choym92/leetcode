class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return max([len(word) for word in s.split(" ")])


checker = Solution()
s = "Hello World"
s1 = "   fly me   to   the moon  "
checker.lengthOfLastWord(s1)
