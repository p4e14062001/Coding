'''
Links:
1. Geeks for Geeks: https://practice.geeksforgeeks.org/explore/?category%5B%5D=Geometric&page=1&category%5B%5D=Geometric
2. Lintcode: https://www.lintcode.com/problem-tag/434/
3. CSES: https://cses.fi/dt/task/315
4. Leetcode: https://leetcode.com/problemset/all/?topicSlugs=geometry
5. Timus: https://acm.timus.ru/problemset.aspx?space=1&tag=geometry
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
    '''
    def circleTouch(self,X1,Y1,R1,X2,Y2,R2):
        return int(((X2 - X1) ** 2 + (Y2  - Y1) ** 2) ** 0.5 <= (R1 + R2))
    '''
    https://practice.geeksforgeeks.org/problems/rectangles-in-a-circle0457/1
    '''
    def rectanglesInCircle(self,r):
        x = 0
        for i in range(1, 2 * r + 1):
            for j in range(1, 2 * r + 1):
                if i * i + j * j <= 4 * r * r:
                    x = x + 1
        return x
    '''
    https://practice.geeksforgeeks.org/problems/check-if-two-line-segments-intersect0017/1/
    '''
    def doIntersect(self, p1, q1, p2, q2):
        m1 = ((p1[1] - q1[1]) * (p1[0] - q2[0])) - ((p1[1]-q2[1])*(p1[0] - q1[0]))
        m2 = ((p1[1] - q1[1]) * (p1[0] - p2[0])) - ((p1[1]-p2[1])*(p1[0] - q1[0]))
        m3 = ((p2[1] - q2[1])* (p2[0] - p1[0])) - ((p2[1] - p1[1])*(p2[0]-q2[0]))
        m4 = ((p2[1] - q2[1])*(p2[0] - q1[0])) - ((p2[1] - q1[1])*(p2[0] - q2[0]))
        if (m1 > 0 and m2 < 0  or m1 < 0  and m2 > 0) and (m3 > 0 and m4 < 0  or m3 < 0  and m4 > 0) : 
            return 1
        elif m1 == 0 and q2[0] <= max(p1[0],q1[0]) and q2[0] >= min (p1[0],q1[0]) and q2[1] <= max (p1[1],q1[1]) and q2[1] >= min (p1[1],q1[1]):
            return 1
        elif m2 == 0 and p2[0] <= max(p1[0],q1[0]) and p2[0] >= min (p1[0],q1[0]) and p2[1] <= max(p1[1],q1[1]) and p2[1] >= min (p1[1],q1[1]):
            return 1
        elif m3== 0 and p1[0] <= max(p2[0],q2[0]) and p1[0] >= min(p2[0],q2[0]) and  p1[1] <= max(p2[1],q2[1]) and p1[1] >= min(p2[1],q2[1]):
            return 1 
        elif m4== 0 and q1[0] <= max(p2[0],q2[0]) and q1[0] >= min(p2[0],q2[0]) and  q1[1] <= max(p2[1],q2[1]) and q1[1] >= min(p2[1],q2[1]):
            return 1
        else:
            return 0
    '''
    https://practice.geeksforgeeks.org/problems/area-of-intersection-of-two-circles0653/1
    '''
    def intersectionArea(self,X1,Y1,R1,X2,Y2,R2):
        pi=3.14
        d=math.sqrt((X1-X2)**2+(Y1-Y2)**2)
        if(d>=(R1+R2)):
            return 0
        elif(d<=abs(R1-R2)):
            if(R1>=R2):
                return round(pi*R2**2,6)
            else:
                return round(pi*R1**2,6)
        else:
            a=(R1**2)*math.acos((d**2+R1**2-R2**2)/(2*d*R1))
            b=(R2**2)*math.acos((d**2+R2**2-R1**2)/(2*d*R2))
            c=0.5*math.sqrt((-d+R1+R2)*(d+R1-R2)*(d-R1+R2)*(d+R1+R2))
            return round(a+b-c,6)
    '''
    https://community.topcoder.com/stat?c=problem_statement&pm=7766
    '''
    def possibleLocations(x1, y1, r1, x2, y2, r2):
        sr = (r1 + r2) ** 2
        dr = (r1 - r2) ** 2
        d = (x2 - x1) ** 2 + (y2 - y1) ** 2
        if x1 == x2 and y1 == y2 and r1 == r2:
            return -1
        if d < dr or d > sr:
            return 0
        if d == sr or d == dr:
            return 1
        if d > dr and d < sr:
            return 2
