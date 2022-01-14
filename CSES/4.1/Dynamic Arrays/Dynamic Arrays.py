class DynammicArrays_4_1:
    def __init__(self, size, initial = 0):
        self.arr = [initial for _ in range(size)]
    def push_back(self, element):
        self.arr.append(element)
    def print_arr(self):
        print(self.arr)
    def access_element(self, index):
        return self.arr[index]
    def back(self):
        return self.arr[-1]
    def pop_back(self):
        self.arr = self.arr[:-1]
