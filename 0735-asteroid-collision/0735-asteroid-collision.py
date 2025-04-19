class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)
        for x in range(n):
            if len(stack) == 0:
                stack.append(asteroids[x])
                continue

            right = asteroids[x]
            left = stack.pop()

            checking = 0
            if left > 0 and right < 0:
                while left > 0 and right < 0:
                    if left != abs(right):
                        if left > abs(right):
                            stack.append(left)
                        else:
                            stack.append(right)
                    if len(stack) > 1:
                        checking = 1
                        right = stack.pop()
                        left = stack.pop()
                    else:
                        checking = 0
                        break
                if checking == 1:
                    stack.append(left)
                    stack.append(right)
            else:
                stack.append(left)
                stack.append(right)
            
        m = len(stack)
        res = [0] * m
        for x in range(m-1, -1, -1):
            res[x] = stack.pop()

        return res