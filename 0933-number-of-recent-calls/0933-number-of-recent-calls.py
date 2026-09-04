class RecentCounter(object):
    def __init__(self):
        self.requests = []
        self.left = 0

    def ping(self, t):
        self.requests.append(t)

        while self.requests[self.left] < t - 3000:
            self.left += 1

        return len(self.requests) - self.left