class Solution:
    def closestPrimes(self,left, right):
        if left > right:
            return [-1, -1]
        a = [True] * (right + 1)
        a[0] = a[1] = False
        for i in range(2, int(math.sqrt(right)) + 1):
            if a[i]:
                for j in range(i * i, right + 1, i):
                    a[j] = False
        x = [i for i in range(left, right + 1) if a[i]]
        if len(x) < 2:
            return [-1, -1]
        return min(zip(x, x[1:]), key=lambda p: p[1] - p[0])
