import random

def main():

    
    secret_code = random.choice(["X","Z","Z"])
    ai = "SECRET CODE"
    print(f'┌{"─"*(len(ai)+2)}┐\n│ {ai} │\n└{"─"*(len(ai)+2)}┘')

    payload = input("what is your name ").strip().upper()

    is_compromised = any(char in payload for char in [
        '$', '%', '#', '@', '!', '&', '*', '(', ')',
        '{', '}', '[', ']', '<', '>', '/', '\\',
            '|', '^', '~'])

    token = (payload)
    is_safe = all([len(token) >= 8, token.isalnum(), not is_compromised])

    if is_safe:
        random_suffix = int(random.random()*999)
        token = f'{payload}_{random_suffix}_{secret_code}'
        print(f"[ACCESS GRANTED] your secure code is : {token}")

    else:
        print('/n[SECURITY ALERT]')
if __name__ == "__main__":
    main()