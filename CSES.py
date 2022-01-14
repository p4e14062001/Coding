class CSES:
    '''
    https://cses.fi/dt/task/312
    https://practice.geeksforgeeks.org/problems/addition-of-two-numbers0812/1
    '''
    def amount(self, a, b):
        return a + b
    '''
    https://cses.fi/dt/task/313
    '''
    def algorithm(self, a):
        while a != 1:
            print(a, end = ' ')
            if a % 2 == 0:
                a = a // 2
            else:
                a = 3 * a + 1
        print(1)
    '''
    https://cses.fi/dt/task/314
    '''
    def bit_strings(self, n):
        return 2 ** n
    '''
    https://cses.fi/dt/task/316
    https://practice.geeksforgeeks.org/problems/day-of-the-week1637/1/
    https://leetcode.com/problems/day-of-the-week/
    https://www.lintcode.com/problem/2661/
    '''
    def day_from_date(self, s):
        s = s.split('.')
        day = int(s[0])
        month = int(s[1])
        year = int(s[2])
        k = day
        m = month - 2
        if m <= 0:
            m = m + 12
        C = year // 100
        Y = year % 100
        if month == 1 or month == 2:
            Y = Y - 1
        W = (k + int(2.6 * m - 0.2) - 2 * C + Y + Y // 4 + C // 4) % 7
        days = ["sunnuntai", "maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai"]
        return days[W]
    '''
    https://cses.fi/dt/task/317/
    '''
    def max_repeat(self, s):
        s = input()
        m = float('-inf')
        c = 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                c = c + 1
            else:
                m = max(m, c)
                c = 1
        return max(m, c)
    '''
    https://cses.fi/dt/task/318/
    '''
    def miss(self, n, s):
        S = 0
        for i in range(n - 1):
            S = S + int(s[i])
        return (n * (n + 1) // 2 - S)
    '''
    https://cses.fi/dt/task/319/
    https://cses.fi/problemset/task/1071/
    '''
    def spiral(self, c):
        c = c.split()
        x = int(c[0])
        y = int(c[1])
        ans = 0
        if y > x:
            if y % 2 != 0:
                ans = y * y - x + 1
            else:
                ans = (y - 1) * (y - 1) + x
        else:
            if x % 2 == 0:
                ans = x * x - y + 1
            else:
                ans = (x - 1) * (x - 1) + y
        return ans
    '''
    https://cses.fi/dt/task/320
    '''
    def knight(self, n):
        return (n * n * (n * n - 1) // 2) - 4 * (n - 1) * (n - 2)
    '''
    https://cses.fi/dt/task/321/
    '''
    def zeros(self, n):
        z = 0
        while n != 0:
            n = n // 5
            z = z + n
        return z
    '''
    https://cses.fi/dt/task/322/
    '''
    def customers(self, s):
        a = []
        d = []
        while t:
            s = s.split()
            a.append(int(s[0]))
            d.append(int(s[1]))
            t = t - 1
        checka = {}
        checkd = {}
        for i in a:
            if i not in checka:
                checka[i] = 0
            checka[i] = checka[i] + 1
        for i in d:
            if i not in checkd:
                checkd[i] = 0
            checkd[i] = checkd[i] - 1
        timeline = sorted(list(checka.items()) + list(checkd.items()))
        m = float('-inf')
        c = 0
        for i in timeline:
            c = c + i[1]
            m = max(m, c)
        return m
    '''
    https://cses.fi/dt/task/323/
    '''
    def deals(self, s, w, a):
        s = s.split()
        n = int(s[0])
        m = int(s[1])
        k = int(s[2])
        w = w.split()
        for i in range(n):
            w[i] = int(w[i])
        a = a.split()
        for i in range(m):
            a[i] = int(a[i])
        w.sort()
        a.sort()
        wishi = 0
        geti = 0
        deal = 0
        while wishi != n and geti != m:
            if w[wishi] - a[geti] > k:
                geti = geti + 1
            elif abs(w[wishi] - a[geti]) <= k:
                geti = geti + 1
                wishi = wishi + 1
                deal = deal + 1
            elif w[wishi] - a[geti] < - k:
                wishi = wishi + 1
        return deal
    '''
    https://cses.fi/dt/task/324
    '''
    def ferris(self, s, w):
        s = s.split()
        n = int(s[0])
        M = int(s[1])
        w = w.split()
        for i in range(n):
            w[i] = int(w[i])
        w.sort()
        start = 0
        end = n - 1
        baskets = 0
        while start <= end:
            baskets = baskets + 1
            if start != end:
                if w[start] + w[end] > M:
                    end = end - 1
                else:
                    start = start + 1
                    end = end - 1
            else:
                break
        return baskets
    '''
    https://cses.fi/dt/task/325
    '''
    def factory(self, s, t):
        s = s.split()
        n = int(s[0])
        p = int(s[1])
        t = t.split()
        for i in range(n):
            t[i] = int(t[i])
        m = max(t)
        left = 0
        right = m * p + 1
        ans = 0
        current_p = 0
        while left <= right:
            mid = left + (right - left) // 2
            current_p = 0
            for i in range(n):
                current_p = current_p + mid // t[i]
            if current_p >= p:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
    '''
    https://cses.fi/dt/task/609/
    '''
    def order(self, n, s):
        n = int(n)
        s = s.split()
        for i in range(n):
            s[i] = int(s[i])
        expected = n
        for i in range(n - 1, -1, -1):
            if s[i] == expected:
                expected = expected - 1
        return expected
    '''
    https://cses.fi/dt/task/326
    '''
    def partition(self, S, s):
        S = S.split()
        n = int(S[0])
        k = int(S[1])
        s = s.split()
        for i in range(n):
            s[i] = int(s[i])
        left = max(s)
        right = sum(s)
        ans = 0
        while left <= right:
            mid = int(left + (right - left) / 2)
            sa = 1
            sums = 0
            for i in range(n):
                sums = sums + s[i]
                if sums > mid:
                    sa = sa + 1
                    sums = s[i]
            if sa <= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
