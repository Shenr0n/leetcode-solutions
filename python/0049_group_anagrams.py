class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for strVal in strs:
            strKey = ''.join(sorted(strVal))
            anagramMap[strKey].append(strVal)

        return list(anagramMap.values())
        
