'''
Links:
1. Geeks for Geeks: https://practice.geeksforgeeks.org/explore/?category%5B%5D=Geometric&page=1&category%5B%5D=Geometric
2. Lintcode: https://www.lintcode.com/problem-tag/434/
3. CSES: https://cses.fi/dt/task/315
4. Leetcode: https://leetcode.com/problemset/all/?topicSlugs=geometry
'''
class Geometry:
    '''
    https://cses.fi/dt/task/315
    '''
    def volume(self, r):
        import math
        return (math.pi) * (4 / 3) * (r ** 3)
    '''
    https://practice.geeksforgeeks.org/problems/line-passing-through-2-points5031/1
    '''
    def getLine(self, a, b, c, d):
        x1 = a
        x2 = c
        y1 = b
        y2 = d
        c1 = (y2 - y1)
        c2 = (x1 - x2)
        c = x1 * (y2 - y1) - y1 * (x2 - x1)
        if c2 >= 0:
            return (str(c1) + "x+" + str(abs(c2)) + "y=" + str(c))
        else:
            return (str(c1) + "x-" + str(abs(c2)) + "y=" + str(c))
    '''
    https://practice.geeksforgeeks.org/problems/number-of-diagonals1020/1
    '''
    def diagonals(self, n):
        if n % 2 == 0:
            return (n // 2) * (n - 3)
        else:
            return ((n - 3) // 2) * n
    '''
    https://practice.geeksforgeeks.org/problems/find-perimeter-of-shapes/1
    '''
    def findPerimeter(arr, n, m):
        x = 0
        for i in range(n):
            flag = 0
            for j in range(m):
                if flag == 0 and arr[i][j] == 1:
                    flag = 1
                    x = x + 1
                if flag == 1 and arr[i][j] == 0:
                    flag = 0
        for j in range(m):
            flag = 0
            for i in range(n):
                if flag == 0 and arr[i][j] == 1:
                    flag = 1
                    x = x + 1
                if flag == 1 and arr[i][j] == 0:
                    flag = 0
        return x * 2
    '''
    https://practice.geeksforgeeks.org/problems/distance-between-2-points3200/1
    '''
    def distance(self, x1, y1, x2, y2):
		return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    '''
    https://practice.geeksforgeeks.org/problems/circle-and-lattice-points4257/1
    '''
    def latticePoints(self, r):
        if r == 0:
            return 0
        x = 0
        for i in range(r + 1):
            if int((r ** 2 - i ** 2) ** 0.5) ** 2 + i ** 2 == r ** 2:
                if i == 0 or r * r - i * i == 0:
                    x = x + 2
                else:
                    x = x + 4
        return x
    '''
    https://practice.geeksforgeeks.org/problems/checcheck-if-two-given-circles-touch-each-other5038/1
    https://www.spoj.com/problems/CIRCINT/
    '''
    def circleTouch(self,X1,Y1,R1,X2,Y2,R2):
        return int(((X2 - X1) ** 2 + (Y2  - Y1) ** 2) ** 0.5 <= (R1 + R2))
    '''
    https://practice.geeksforgeeks.org/problems/rectangles-in-a-circle0457/1
    '''
