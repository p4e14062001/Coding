class Dynamic Programming:
    '''
    https://leetcode.com/problems/coin-change/ ---> MEDIUM
    '''
    def solve(self, amount, coins):
        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0
        m = float('inf')
        for i in coins:
            m = min(m, self.solve(amount - i, coins) + 1)
        return m
    def coinChangeRecursion(self, coins, amount):
        ans = self.solve(amount, coins)
        if ans == float('inf'):
            return -1
        return ans
    '''
    https://leetcode.com/problems/coin-change/ ---> MEDIUM
    '''
    def solve(self, amount, coins, ready, values):
        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0
        if ready[amount]:
            return values[amount]
        m = float('inf')
        for i in coins:
            m = min(m, self.solve(amount - i, coins, ready, values) + 1)
        ready[amount] = True
        values[amount] = m
        return m
    def coinChangeMemoization(self, coins, amount):
        ans = self.solve(amount, coins, [False for _ in range(amount + 1)], [-1 for _ in range(amount + 1)])
        if ans == float('inf'):
            return -1
        return ans
    '''
    https://leetcode.com/problems/coin-change/ ---> MEDIUM
    '''
    def solve(self, amount, coins, values):
        values[0] = 0
        for j in range(1, amount + 1):
            values[j] = float('inf')
            for i in range(len(coins)):
                if j - coins[i] >= 0:
                    values[j] = min(values[j], values[j - coins[i]] + 1)
        return values[-1]
    def coinChangeIteration(self, coins, amount):
        ans = self.solve(amount, coins, [float('inf') for _ in range(amount + 1)])
        if ans == float('inf'):
            return -1
        return ans
    '''
    https://leetcode.com/problems/coin-change/ ---> MEDIUM
    '''
    def solve(self, amount, coins, values):
        for i in range(len(values)):
            for j in range(len(values[0])):
                if j == 0:
                    values[i][j] = 0
                elif coins[i - 1] <= j:
                    values[i][j] = min(values[i - 1][j], values[i][j - coins[i - 1]] + 1)
                else:
                    values[i][j] = values[i - 1][j]
        return values[-1][-1]
    def coinChangeTabulation(self, coins, amount):
        ans = self.solve(amount, coins, [[float('inf') for _ in range(amount + 1)] for _ in range(len(coins) + 1)])
        if ans == float('inf'):
            return -1
        return ans
