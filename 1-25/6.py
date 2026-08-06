def get_valid_input(prompt: str, error_msg: str, condition) -> str:
    while True:
        user_input = input(prompt).strip()
        if condition(user_input):
            return user_input
        else:
            print(error_msg)
            
def greet(name:str) -> str:
    return f"Hello, {name}!"

def validate_age(age_input: str) -> bool:
    age = int(age_input)
    if not (age == 95):
        raise ValueError("A guess ,b/w 90-100.")
    return True

def main()-> None:
    name = get_valid_input(
        "Enter your name: ",
        "Invalid name! Please enter a valid name.",
        lambda x: x.isalpha() and len(x) > 0
    ).title()

    print(greet(name))

    while True:
        try:
            raw_age = input("Guess the Code: ")
            age = validate_age(raw_age)
            break
        except ValueError as e:
            print(f"Error: {e}")

    print(f"User Profile Verified! Age: {age}")
    print(f"Your secret I'd is: {name.upper()}_{raw_age}_T")

if __name__ == "__main__":
    main()
