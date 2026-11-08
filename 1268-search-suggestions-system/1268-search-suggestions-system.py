class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        res = []
        prefix = ""
        for c in searchWord:
            prefix += c
            suggestions = []
            for i in products:
                if i.startswith(prefix):
                    suggestions.append(i)
                if len(suggestions) == 3:
                    break
            res.append(suggestions)
        return res