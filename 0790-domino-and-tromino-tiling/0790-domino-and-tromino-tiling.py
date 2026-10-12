class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9 + 7

        
        pcache, ncache = {}, {}
        def p(n):
            if n == 2:
                return 1
            if n in pcache:
                return pcache[n]
            pcache[n] = p(n-1) + f(n-2)
            return pcache[n]
        def f(n):
            if n <= 2:
                return n
            if n in  ncache:
                return ncache[n]
            ncache[n] = f(n-1)+f(n-2)+2*p(n-1)
            return ncache[n]
        return f(n)%mod