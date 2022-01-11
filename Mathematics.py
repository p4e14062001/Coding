class Mathematics:
	def sum_numbers_power1(self, n):
		return (n * (n + 1)) // 2
	def sum_numbers_power2(self, n):
		return (n * (n + 1) * (2 * n + 1)) // 6
	def sum_numbers_power3(self, n):
		return self.sum_numbers_power1(n) ** 2
m = Mathematics()
s = int(input())
print(m.sum_numbers_power1(s))
print(m.sum_numbers_power2(s))
print(m.sum_numbers_power3(s))
