**Digital Memory Jar**

Hi! 👋 I’ve been learning Python for a few weeks and wanted to build something that’s a bit different — not just another calculator or guessing game.

So I made the Digital Memory Jar — a small Python project that lets you record how your day went, save it, and look back at your memories later. It’s like a personal diary that turns your thoughts into data.

**🌟 What It Does**

Every time you run the program, it asks you:

How your mood was (1–10)

The best part of your day

Your biggest challenge

It then saves your answers (with today’s date) into a file.
Later, you can view all your past memories in one place.

Example output:

🪣 Welcome to your Digital Memory Jar!
1. Add Memory  2. View Memories  3. Quit
> 2
2025-10-27 | Mood: 8 | 😊 Finished my project | ⚡ Focusing

**💾 Features**

🧠 Add daily memories

📅 Automatically includes today’s date

💾 Saves entries to a CSV file (memories.csv)

🔍 View all past memories in an easy-to-read format

📂 Keeps your data safe so you can look back anytime

**🧰 Tools & Skills Used**

Python 3

csv module — to save and read your data

datetime — to get the current date

Learned about:

Functions

Loops

If statements

File handling

User input

This project helped me understand how small parts of Python come together to make something that actually works.

**🚀 How to Run**
**💻 Run on Your Computer**

Copy the code into a file called main.py

Open your terminal or command prompt

Type:

python main.py


Choose an option from the menu (Add / View / Quit)

**🌐 Run Online**

If you don’t have Python installed, you can run it directly on Replit
.

**🧩 Example of the Code**
def add_memory():
    date = datetime.now().strftime("%Y-%m-%d")
    mood = input("Mood (1-10): ")
    highlight = input("Best part of your day: ")
    challenge = input("Biggest challenge: ")

    with open("memories.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood, highlight, challenge])
    print("Memory saved successfully!\n")


This is the part that asks you questions and saves your answers in a file — like writing in your own diary.

**💡 Future Plans**

I want to add a few more features later, such as:

📈 Graphs to show mood changes over time (using matplotlib)

🔒 Password protection so entries stay private

🪞 A “year in review” summary (how many good days you had)

🌤 Integration with a weather API to show what the weather was like each day

**❤️ Why I Made This**

I made this project to practice Python in a way that felt personal and creative.
It’s a simple idea, but it shows how programming can turn something meaningful — like your emotions and memories — into data you can interact with.

For me, this project represents the start of my learning journey in Python and my interest in building small, personal tools that make everyday life a bit more interesting.

**📂 Folder Layout**
digital_memory_jar/
│
├── main.py
├── memories.csv   # created automatically after first run
└── README.md

**📜 License**

This project is open-source — feel free to use, edit, and learn from it!

**✨ Final Notes**

This is one of my first Python projects, and I’m proud of how it turned out.
It helped me understand that programming isn’t just about math or numbers — it’s about building things that connect with people, even in small ways.

**Shrish Umamaheswaran**
