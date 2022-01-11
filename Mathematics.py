class Mathematics:
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
m = Mathematics()
n = int(input("Input number of natural numbers\n"))
print("Input number of natural numbers", n)
print("Sum of power 1 is", m.sum_numbers_power1(n))
print("Sum of power 2 is", m.sum_numbers_power2(n))
print("Sum of power 3 is", m.sum_numbers_power3(n))
p = int(input("Input power on each natural number\n"))
print("Power entered is", p)
print("Sum of power of natural numbers is", m.sum_numbers_powerk(n, p))
arr = input("Enter array\n").split()
n = len(arr)
for i in range(n):
	arr[i] = int(arr[i])
print("Array input is", arr)
option = input("Want to check if array is AP (Y/N)?\n")
if option == 'Y':
	if m.check_ap(arr):
		print("Array is an AP")
		option = input("Want to find sum and common difference (Y/N)?\n")
		if option == 'Y':
			print("Sum of the AP is", m.sum_ap(arr))
			print("Common difference of the AP is", arr[1] - arr[0])
	else:
		print("Array is not an AP")
option = input("Want to check if array is GP (Y/N)?\n")
if option == 'Y':
	if m.check_gp(arr):
		print("Array is a GP")
		option = input("Want to find sum and common ratio (Y/N)?\n")
		if option == 'Y':
			print("Sum of the GP is", m.sum_gp(arr))
			print("Common ratio of the GP is", arr[1] / arr[0])
	else:
		print("Array is not a GP")
