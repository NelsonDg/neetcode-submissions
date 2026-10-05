class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # notebook: how many of each letter are in the window
        res = 0  # high score: longest good window found so far

        l = 0  # left finger starts at the first letter
        maxf = 0  # most times any one letter has appeared in the window
        for r in range(len(s)):  # move right finger one letter at a time
            count[s[r]] = 1 + count.get(s[r], 0)  # add 1 to this letter's tally (start at 0 if new)
            maxf = max(maxf, count[s[r]])  # update the biggest letter group if this one is bigger

            while (r - l + 1) - maxf > k:  # need more repaints than k allows? window is too big
                count[s[l]] -= 1  # left letter leaves the window, so take 1 off its tally
                l += 1  # move left finger right to shrink the window
            res = max(res, r - l + 1)  # save window size if it beats the high score

        return res  # the longest window we could make all one letter