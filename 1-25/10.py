class SecurityValidationError(Exception):
    pass

class SovereignGameEngine:
    def __init__(self, player_name: str):
        self.player = player_name
        self.energy = 100

    def consume_energy(self, energy_cost: int):
        is_valid = lambda cost: 0 < cost <= self.energy
        
        if not is_valid(energy_cost):
            raise SecurityValidationError("Invalid input or energy deficit!")
            
        self.energy -= energy_cost
        return f"{self.player} consumed {energy_cost} energy. Remaining: {self.energy}"

if __name__ == "__main__":
    name = input("Enter your Player Name: ")
    game = SovereignGameEngine(name)
    
    print(f"Welcome {game.player}! Your current energy is: {game.energy}")
    
    try:
        cost = int(input("Enter energy cost to consume: "))
        output = game.consume_energy(cost)
        print(f"✅ {output}")
    except ValueError:
        print("🛡️ Error: Please enter a valid integer number!")
    except SecurityValidationError as err:
        print(f"🛡️ Security Alert: {err}")