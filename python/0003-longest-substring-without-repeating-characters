class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        op = 0
        left = 0
        charSet = set()

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            op = max(op, right - left + 1)
        return op