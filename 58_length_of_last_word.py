class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len([word.strip() for word in s1.split(" ") if word.strip()][-1])


checker = Solution()
s = "Hello World"
s1 = "   fly me   to   the moon  "
checker.lengthOfLastWord(s1)