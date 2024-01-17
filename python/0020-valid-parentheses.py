class Solution:
    def isValid(self, s: str) -> bool:
        pStack = []
        pMap = {")":"(", "]":"[", "}":"{"}

        for string in s:
            if string in pMap:
                if pStack and pStack[-1] == pMap[string]:
                    pStack.pop()
                else:
                    return False
            else:
                pStack.append(string)
        
        return pStack == []

        
