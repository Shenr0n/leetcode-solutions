class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        op = 0
        maxcount = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0) + 1

            maxcount = max(maxcount, count[s[right]])
            #window length - max in count values
            #if (right-left+1) - max(count.values()) > k:
            if (right-left+1) - maxcount > k:
                count[s[left]] -= 1
                left += 1

            op = max(op, right-left+1)
        return op
                


    