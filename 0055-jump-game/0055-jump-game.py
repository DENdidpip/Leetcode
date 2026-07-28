class Solution(object):
    def canJump(self, nums):
        target = len(nums) - 1
        visited = set()

        def step(pos):
            if pos == target:
                return True

            if pos in visited:
                return False

            visited.add(pos)

            for jump in range(nums[pos], 0, -1):
                next_pos = pos + jump

                if next_pos <= target:
                    if step(next_pos):
                        return True

            return False

        return step(0)