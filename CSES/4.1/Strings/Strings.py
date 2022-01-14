class String_4_1:
    def make(self, size, initial = '.'):

    def add(self, a, b):
        return a + b
    def subs(self, s, start, end):
        if end != len(s):
            return s[start: end + 1]
        return s[start:]
    def change(self, s, char, index):
        s = list(s)
        s[index] = char
        return ''.join(s)
