class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        s1_freq: dict[str, int] = {}
        s2_freq: dict[str, int] = {}

        for i in range(len(s1)):
            s1_freq[s1[i]] = s1_freq.get(s1[i], 0) + 1
            s2_freq[s2[i]] = s2_freq.get(s2[i], 0) + 1

        i, j = 0, len(s1) - 1
        while True:
            if s1_freq == s2_freq:
                return True
            
            s2_freq[s2[i]] -= 1
            if s2_freq[s2[i]] == 0:
                del s2_freq[s2[i]]

            i += 1
            j += 1

            if j >= len(s2):
                break
            
            s2_freq[s2[j]] = s2_freq.get(s2[j], 0) + 1
        
        return False