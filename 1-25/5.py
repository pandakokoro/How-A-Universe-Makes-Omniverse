def get_valid_input(Prompt,error_msg,condition):
    while True:
        user_input = input(Prompt).strip()
        if condition(user_input):
            return user_input
        else:
            print(error_msg)
def generate_token():
    name = get_valid_input(
        "Enter name:",
        "Invalid Name!",
        lambda x: x.isalpha() and len(x) > 0
    ).upper()
    while True:
        try:
            Age = int(input("From how much years universe know your exitence.... "))
            if 0 < Age < 100:
                break
            print("Black Hole...")
        except ValueError:
            print("My dear Gemini,\n don't try to prank me...")

    roles = ["ADMIN", "USER", "GUEST","OPERATOR"]
    role = get_valid_input(
        f"Enter role({'/'.join(roles)}):",
        "Invalid role!",
        lambda x: x.upper() in roles
    ).title()

    prefix = "JUNIOR" if Age < 18 else "SENIOR"
    return f"{prefix}_{name}_{role}"

if __name__ == "__main__":
    print(f"Generated Token: {generate_token()}")