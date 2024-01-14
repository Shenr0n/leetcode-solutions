class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        anagramArr = [0]*26

        for strVal in s:
            letter = ord(strVal)-ord('a')
            anagramArr[letter] += 1
        
        for strVal in t:
            letter = ord(strVal)-ord('a')
            anagramArr[letter] -= 1

        for strVal in anagramArr:
            if strVal != 0:
                return False
        return True
        