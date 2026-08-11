from functools import reduce
raw_input = input("Enter comma separated numbers: ")
valid_data = list(map(int,filter(lambda s: s.strip().lstrip('-').isdigit(), raw_input.split(','))))
if valid_data:
    pipline_result = reduce(
        lambda acc, x: acc + x,
        map(lambda x: x**2, filter(lambda x:x > 0 ,valid_data)),
        0
    )
    print(f"Sum of squares of positive numbers: {pipline_result}")
else:
    print("No valid positive numbers found.")