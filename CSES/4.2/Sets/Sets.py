'''
1. https://www.w3schools.com/python/python_sets_exercises.asp
'''
class Set_4_2:
    def __init__(self):
        self.sets = {}
    def print_set(self):
        print(self.sets)
    def length(self):
        return len(self.sets)
    def anything_to_set(self, l):
        self.sets = set(l)
    def check(self, element):
        return element in self.sets
    def addition(self, element):
        self.sets.add(element)
    def union_sets(self, setb):
        self.sets.update(setb)
    def intersection_sets(self, setb):
        self.sets.intersection_update(setb)
    def difference_sets(self, setb):
        self.sets.symmetric_difference_update(setb)
    def remove(self, element):
        if element in self.sets:
            self.sets.remove(element)
    def discard(self, element):
        self.sets.discard(element)
    def see_and_remove_last(self, element):
        x = self.sets.pop()
        return x
    def empty_set(self):
        self.sets.clear()
    def delete_set(self):
        del self.sets
    def union(self, setb):
        return self.sets.union(setb)
    def intersection(self, setb):
        return self.sets.intersection(setb)
    def difference(self, setb):
        return self.sets.symmetric_difference(setb)
    def duplicate(self):
        return self.sets.copy()
    def disjoint(self, setb):
        return self.sets.isdisjoint(setb)
    def subset(self, setb):
        return self.sets.issubset(setb)
    def superset(self, setb):
        return self.sets.issuperset(setb)
