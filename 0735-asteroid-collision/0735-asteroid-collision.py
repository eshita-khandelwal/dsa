class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        #an astroid will only collide if we have a positive value on the top of the stack and a negative value as a curr astroid
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                w = stack[-1] + a
                if w < 0:
                    stack.pop()
                elif w > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack