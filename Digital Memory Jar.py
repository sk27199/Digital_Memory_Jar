import csv
from datetime import datetime
import random  # 👈 needed for random quotes


# 💬 This function picks a random motivational quote
def random_quote():
    quotes = [
        "Keep going, you’re doing great!",
        "Every small step counts.",
        "You made it through today — that’s enough.",
        "Progress, not perfection 💪",
        "You’re stronger than you think.",
        "Small steps lead to big change 🌱",
        "You showed up today, and that matters ❤️"
    ]
    print("\n💬 " + random.choice(quotes) + "\n")


# 🪣 This function adds a new memory entry
def add_memory():
    date = datetime.now().strftime("%Y-%m-%d")  # gets today’s date
    mood = input("Mood (1-10): ")  # asks user for their mood number
    highlight = input("Best part of your day: ")  # what went well
    challenge = input("Biggest challenge: ")  # what was difficult

    # Opens (or creates) memories.csv and adds a new line
    with open("memories.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood, highlight, challenge])
    print("Memory saved successfully!\n")

    # 👇 After saving, show a random motivational quote
    random_quote()


# 👀 This function shows all saved memories
def view_memories():
    try:
        with open("memories.csv", "r") as file:
            reader = csv.reader(file)
            print("\n📜 Your Saved Memories:\n")
            for row in reader:
                if not row:  # skips blank rows
                    continue
                print(f"{row[0]} | Mood: {row[1]} | 😊 {row[2]} | ⚡ {row[3]}")
            print()  # adds a blank line after listing
    except FileNotFoundError:
        print("No memories found yet. Try adding one first!\n")


# 🧠 The main program loop (menu)
def main():
    print("🪣 Welcome to your Digital Memory Jar!")
    while True:
        print("1. Add Memory  2. View Memories  3. Quit")
        choice = input("> ")

        if choice == "1":
            add_memory()
        elif choice == "2":
            view_memories()
        elif choice == "3":
            print("Goodbye! 👋 Come back soon to add more memories.")
            break
        else:
            print("Invalid choice, try again.\n")


# 🚀 Runs the main program
if __name__ == "__main__":
    main()

