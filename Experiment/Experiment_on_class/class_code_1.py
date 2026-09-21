from typing import List


class solution:
    def fuzz_buzz_matrix(self, n: int) -> List[str]:
        result = []
        for number in range(1, n + 1):
            if number % 15 == 0:
                result.append("FizzBuzz")
            elif number % 3 == 0:
                result.append("Fizz")
            elif number % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(number))
        return result

if __name__ == "__main__" :
    print(solution().fuzz_buzz_matrix(15))