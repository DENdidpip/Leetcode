from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        radiant = deque()
        dire = deque()
        n= len(senate)
        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                # R ходит раньше D
                radiant.append(r + n)
            else:
                # D ходит раньше R
                dire.append(d + n)

        if radiant:
            return "Radiant"
        else:
            return "Dire"