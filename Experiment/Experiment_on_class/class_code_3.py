import numpy as np
import random as rd

from typing import List

arr = np.random.choice(10, size=9, replace=False) + 1

class solution:
    def smaller_number_than_current(self, nums: List[int]) -> List[int]:
        self = arr
        ans = []
        for i in nums :
            c = 0
            for j in nums :
                if j<i:
                    c += 1
            ans.append(c)
        return ans

if __name__ == "__main__" :
    print(f"\n \nThe Original ARRAY :\n \n{arr}\n")
    print(f"The smaller numbers than the current number :\n \n{solution().smaller_number_than_current([int(value) for value in arr])}\n")