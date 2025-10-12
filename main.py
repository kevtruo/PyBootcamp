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

print(f"Welcome to PyBootcamp, an interactive Python learning program which operates out of the CLI.")
username = input(f"Enter your name: ")
print(f"Welcome {username}!")