from functools import reduce

class SecurityValidationError(Exception):
    pass

def validate(value: str, condition, message: str) -> str:
    value = value.strip()
    if not condition(value):
        raise SecurityValidationError(message)
    return value

def build_engine(*values: int, **config: int) -> dict:
    valid = list(filter(lambda x: x > 0, values))
    power = reduce(lambda a, x: a + x ** 2, valid, 0)
    return {"power": power, **config}

def main() -> None:
    try:
        name = validate(
            input("Enter identity: "),
            lambda x: x.isalpha() and len(x) >= 3,
            "Invalid identity."
        ).upper()

        raw = input("Enter energy values: ").split(",")
        values = tuple(map(int, raw))

        age = int(input("Enter age: "))
        if not 1 <= age <= 100:
            raise SecurityValidationError("Invalid age.")

        role = validate(
            input("Enter role: "),
            lambda x: x.upper() in {"ADMIN", "USER", "OPERATOR"},
            "Unauthorized role."
        ).upper()

        engine = build_engine(*values, name=name, age=age, role=role)
        token = f"{role}_{name}_{engine['power']}_{'JUNIOR' if age < 18 else 'SENIOR'}"

        print(f"ENGINE ONLINE: {token}")

    except (ValueError, SecurityValidationError) as error:
        print(f"SECURITY ALERT: {error}")

if __name__ == "__main__":
    main()