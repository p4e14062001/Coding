class Mathematics:
	def sum_numbers_power1(self, n):
		return (n * (n + 1)) // 2
	def sum_numbers_power2(self, n):
		return (n * (n + 1) * (2 * n + 1)) // 6
	def sum_numbers_power3(self, n):
		return self.sum_numbers_power1(n) ** 2
	def sum_numbers_powerk(self, n, k):
		s = 0
		for i in range(1, n + 1):
			s = s + i ** k
		return s
m = Mathematics()
n = int(input("Input number of natural numbers\n"))
print(m.sum_numbers_power1(n))
print(m.sum_numbers_power2(n))
print(m.sum_numbers_power3(n))
p = int(input("Input power on each natural number\n"))
print(m.sum_numbers_powerk(n, p))
