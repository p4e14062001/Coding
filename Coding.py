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

class Dynamic_Programming:
    '''
    https://www.interviewbit.com/problems/0-1-knapsack/
    MEDIUM
    '''
    def knapsack_01(self, values, weights, capacity):
        L = len(values)
        dp = [[0 for _ in range(capacity + 1)] for _ in range(L + 1)]
        for i in range(L + 1):
            for j in range(capacity + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif weights[i] <= j:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[L][capacity]
    '''
    https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1/
    MEDIUM
    '''
    def subset_sum(self, arr, s):
        N = len(arr)
        dp = [[False for _ in range(s + 1)] for _ in range(N + 1)]
        for i in range(N + 1):
            for j in range(s + 1):
                if j == 0:
                    dp[i][j] = True
                elif arr[i] <= j:
                    dp[i][j] = dp[i - 1][j] or (dp[i - 1][j - arr[i]])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[N][s]
    '''
    https://leetcode.com/problems/partition-equal-subset-sum/
    MEDIUM
    '''
    def equal_sum(self, arr):
        s = sum(arr)
        if s % 2 == 0:
            s = s // 2
        else:
            return False
        N = len(arr)
        dp = [[False for _ in range(s + 1)] for _ in range(N + 1)]
        for i in range(N + 1):
            for j in range(s + 1):
                if j == 0:
                    dp[i][j] = True
                elif arr[i] <= j:
                    dp[i][j] = dp[i - 1][j] or (dp[i - 1][j - arr[i]])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[N][s]
