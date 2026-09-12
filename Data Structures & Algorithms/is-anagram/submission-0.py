class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map: dict[str, int] = {}
        t_map: dict[str, int] = {}
        for i in range(len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            t_map[t[i]] = t_map.get(t[i], 0) + 1
        
        for k in s_map.keys():
            if k not in t_map:
                return False
            
            if t_map[k] != s_map[k]:
                return False
        
        return True
