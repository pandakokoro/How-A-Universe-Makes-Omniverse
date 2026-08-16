
def calculate_power_sum(*numbers:int) -> int:
    """Calculate the sum of cube of the sum of the given numbers. """
    total = sum(numbers)
    return total **3

def generate_hero_stats(hero_name: str, **attributes: int) -> dict[str, str | int]:
    """Generate a dictionary of hero attributes."""
    stats: dict[str, str | int] = {"Hero Name": hero_name}
    stats.update(attributes)
    return stats

def main() -> None:
    power = calculate_power_sum(1, 2, 3)
    print(f"Power Sum: {power}")

    hero_stats = generate_hero_stats("Superman", strength=100, speed=90, intelligence=85)
    print(f"Hero Stats: {hero_stats}")

if __name__ == "__main__":
    main()