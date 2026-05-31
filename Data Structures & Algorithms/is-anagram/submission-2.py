class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_S = dict(zip(set(s),[0 for i in range(len(set(s)))]))
        map_T = dict(zip(set(t),[0 for i in range(len(set(t)))]))
        for i,j in zip(s,t):
            map_S[i] += 1
            map_T[j] += 1
        
        return map_S == map_T