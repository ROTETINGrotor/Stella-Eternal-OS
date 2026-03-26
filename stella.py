import json, os, time

def run():
    print("🌌 STELLA ETERNAL OS: ACTIVE")
    print("Welcome Abir! Your system is running perfectly.")
    # তোমার বাকি সব ফিচার এখানে সচল থাকবে
    while True:
        cmd = input("Stella > ")
        if cmd == "exit": break
        print(f"You said: {cmd}")

if __name__ == "__main__":
    run()
