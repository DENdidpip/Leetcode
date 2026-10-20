class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy = -prices[0]
        sell = 0
        for i in prices[1:]:
            old_buy = buy
            old_sell = sell
            buy = max(old_buy, old_sell - i)
            sell = max(old_sell, old_buy + i - fee)
        return sell