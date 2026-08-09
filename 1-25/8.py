import time
def main()-> None:
    print("Connecting to parallel Dimensions", end="", flush=True)
    for _ in range(5):
        time.sleep(0.8)
        print("◄a⌐£►", end="", flush=True)

    ai = "LAMBDA CLASS"
    print(f'\n┌{"─"*(len(ai)+2)}┐\n│ {ai} │\n└{"─"*(len(ai)+2)}┘')

    add_ten = lambda x: x + 10
    print(f"Adding 10 to 5 gives: {add_ten(5)}")

    numbers : list[int] = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print(f"Squared numbers: {squared_numbers}")

if __name__ == "__main__":
    main()