from typing import List
import numpy as np


class CoinChange:
    """
    Since the same sub-problems are called again, the Coin Machine problem has the Overlapping Sub-problems property. 
    So the Coin Change problem has both properties of a Dynamic Programming (DP) problem. Like other typical DP 
    problems, re-computations of the same sub-problems can be avoided by constructing a temporary table[][] in a 
    bottom-up manner. This reduces the brute force Time Complexity of O(2^sum) to O(M*sum) for the DP method. In 
    addition, a method is added to release memory by removing variables related to the solutions of lower numbers 
    where they no longer necessary to achieve better performance. Follow the below steps to Implement the idea: 

    Using 2-D vector to store the Overlapping sub-problems.
    Traversing the whole array to find the solution and storing in the memoization table.
    Using the memoization table to find the optimal solution.
    Release memory of deleting the no longer wanted of sub-problem solutions. 

    Below is the implementation of the above Idea:
    """
    def __init__(
            self,
            coins: List,
            amount: str
    ):
        self.coins = coins
        self.amount = amount

        # Calculating the whole amount in pences
        pounds = int(self.amount[1:].split('-')[0])

        try:
            pences = int(self.amount[1:].split('-')[1])
        except ValueError:
            pences = 0

        self.amount_pence = 100 * pounds + pences

    def coin_change_solutions(self):
        coins = [i for i in self.coins if i <= self.amount_pence]
        S = self.amount_pence

        N = len(coins)
        sols = [[[] for n in range(N + 1)] for s in range(S + 1)]

        for n in range(0, N + 1):
            sols[0][n].append([])
        sols = np.array(sols)

        # fill table using bottom-up dynamic programming
        sols = np.array(sols)
        for s in range(1, S + 1):

            for n in range(1, N + 1):

                without_last = sols[s][n - 1]

                if coins[n - 1] <= s:
                    with_last = [list(sol) + [coins[n - 1]] for sol in sols[s - coins[n - 1]][n]]
                    try:
                        if s > max(coins):
                            # release memory
                            sols[s - coins[n - 1]][n] = []
                    except:
                        pass
                else:
                    with_last = []
                sols[s][n] = without_last + with_last
            try:
                if s > max(coins):
                    # release memory
                    sols[s - max(coins)] = []
            except:
                pass

        counter = 0

        for solution in sols[S][N]:
            if len(solution) % 2 != 0:
                counter += 1

        return counter
