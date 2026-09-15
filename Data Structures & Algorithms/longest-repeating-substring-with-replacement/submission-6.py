class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        res = 0
        frequency_map: dict[str, int] = {}

        should_update = True

        while j < len(s):
            if should_update:
                frequency_map[s[j]] = frequency_map.get(s[j], 0) + 1

            current_len = j - i + 1
            most_frequent = max(frequency_map.values())
            if (current_len - most_frequent) <= k:
                res = max(res, current_len)
                j += 1
                should_update = True
            else:
                frequency_map[s[i]] -= 1
                i += 1
                should_update = False
        
        return res