def welcome_banner():
    banner = r"""
    ____        ____              __                           
   / __ \__  __/ __ )____  ____  / /__________ _____ ___  ____ 
  / /_/ / / / / __  / __ \/ __ \/ __/ ___/ __ `/ __ `__ \/ __ \
 / ____/ /_/ / /_/ / /_/ / /_/ / /_/ /__/ /_/ / / / / / / /_/ /
/_/    \__, /_____/\____/\____/\__/\___/\__,_/_/ /_/ /_/ .___/ 
      /____/                                          /_/      
"""
    print(banner)

if __name__ == "__main__":
    welcome_banner()

print(f"Welcome to PyBootcamp, an interactive, challenge-based Python learning program which operates out of your terminal. ")
username = input(f"Enter your name: ")
print(f"Welcome {username}!")
print(f"...")

table_of_contents = [
    "0. Introduction (START HERE)",
    "1. Variables and Data Types",
    "2. Conditionals (if/else)",
    "3. Loops (for/while)",
    "4. Functions",
    "5. Lists and Dictionaries",
    "6. File I/O",
    "7. Error Handling"
]

def display_menu(toc):
    print("\n=== Available Lessons ===")
    for item in toc:
        print(f"  {item}")
    print("========================\n")

def lesson_introduction():
    print("\n--- Lesson 1: Variables ---")
    print("Each module will have a brief summary of what the module is about followed by a set of challenges that you will need to progress through. PyBootcamp is focused on learning through interacting with a Python program through the terminal, which hopefully will get you more comfortable with running commands. We'll start off with navigating the program itself. Let's begin!")
    print(f"...")
    
    # Interactive exercise
    print("\nTry it: ")
    user_code = input(">>> ")

def lesson_variables():
    print("\n--- Lesson 1: Variables ---")
    print("Variables store data. Syntax: variable_name = value")
    print("\nExample: age = 25")
    
    # Interactive exercise
    print("\nTry it: Create a variable 'favorite_color' with your favorite color")
    user_code = input(">>> ")

#FLOW CONTROL
while True:
    display_menu(table_of_contents)
    choice = input("Select a lesson (1-7) or 'q' to quit: ")
    
    if choice == 'q':
        break
    elif choice == '0':
        lesson_introduction()
    elif choice == '1':
        lesson_variables()

# completed_lessons = set()
# Mark lessons as done
# Show progress percentage