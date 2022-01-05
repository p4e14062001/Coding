class Hash_Sort:
    '''
    https://practice.geeksforgeeks.org/problems/winner-of-an-election-where-votes-are-represented-as-candidate-names-1587115621/1
    EASY
    '''
    def find_winner(self, arr):
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 0
            d[i] = d[i] + 1
        M = max(d.values())
        equal = []
        for i in d:
            if d[i] == M:
                equal.append(i)
        equal = sorted(equal)
        return [equal[0], str(M)]
