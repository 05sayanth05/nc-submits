class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        l, r = 1, max(piles)
        res = r # cause we are trying to find the minimum k

        # checked the solution
        """
        intuition is that the possible rate will be between 1 and max(piles),
        we can search this either brute force or by binary search

        brute force:
        for each element from 1 to max(piles):
            hours = find total time taken by this rate
        check if hours <= the input h, if yes then return the rate (because we are going from
        rate low to high)

        binary search:
        [1, 2, ..., max(piles)]
                ^ - mid
        we check the mid rate and see if it can consume within h if yes we search the left
        part that is right = mid - 1 to see if we can find a min value than the current one
        also we store this currently acceptable one

        if that mid rate cannot consume within h that says we have to increase the rate
        so we search the right part of the array that is left = mid + 1
        """

        while l <= r:
            k = (l + r) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res


