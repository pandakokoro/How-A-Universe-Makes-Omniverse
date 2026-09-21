class solution:
    def count_odds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2

if __name__ == "__main__" :
    low = int(input("Enter low: "))
    high = int(input("Enter high: "))
    print(solution().count_odds(low, high))
