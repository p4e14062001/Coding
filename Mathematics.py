class Mathematics:
	'''
	https://cses.fi/dt/task/312
	'''
	def s(self, a, b):
		return a + b
	'''
	https://cses.fi/dt/task/313
	'''
	def algo(self, a):
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
	def number_n_bits(self, n):
		return 2 ** n
	'''
	https://cses.fi/dt/task/315
	'''
	def volume(self, r):
		import math
		return (math.pi) * (4 / 3) * (r ** 3)
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
	def 
	def sum_numbers_power1(self, n):
		return (n * (n + 1)) / 2
	def sum_numbers_power2(self, n):
		return (n * (n + 1) * (2 * n + 1)) / 6
	def sum_numbers_power3(self, n):
		return self.sum_numbers_power1(n) ** 2
	def sum_numbers_powerk(self, n, k):
		s = 0
		for i in range(1, n + 1):
			s = s + i ** k
		return s
	def check_ap(self, arr):
		n = len(arr)
		for i in range(1, n - 1):
			if arr[i - 1] - arr[i] != arr[i] - arr[i + 1]:
				return False
		return True
	def sum_ap(self, arr):
		n = len(arr)
		return ((arr[0] + arr[-1]) * n) / 2
	def check_gp(self, arr):
		n = len(arr)
		for i in range(1, n - 1):
			if arr[i - 1] / arr[i] != arr[i] / arr[i + 1]:
				return False
		return True
	def sum_gp(self, arr):
		n = len(arr)
		if arr[1] / arr[0] != 1:
		    return ((arr[-1] * (arr[1] / arr[0])) - arr[0]) / ((arr[1] / arr[0]) - 1)
		else:
		    print(n * arr[0])
	def sum_hm(self, n):
		s = 0
		for i in range(1, n + 1):
			s = s + (1 / i)
		return s
	def make_set(self, s):
		return set(s)
	def size_set(self, s):
		return len(s)
	def find(self, s, a):
	    return a in s
