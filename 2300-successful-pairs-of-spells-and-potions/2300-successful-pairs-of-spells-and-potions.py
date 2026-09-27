class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        result = []
        for spell in spells:
            need = (success + spell - 1) // spell

            left = 0
            right = len(potions)
            while left < right:
                mid = (left + right) // 2

                if potions[mid] >= need:
                    right = mid
                else:
                    left = mid + 1
            result.append(len(potions) - left)

        return result
