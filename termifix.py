from colorama import Fore, Style, init
import json
import subprocess
import webbrowser

# Initialize colorama for Linux & Windows terminals
init(autoreset=True, convert=True)

# Load commands from JSON file
with open("commands.json") as f:
    commands = json.load(f)

# Function to display banner (replace logo content with your ASCII art)
def show_banner(system=None):
    logo = r"""
████████╗███████╗██████╗ ███╗   ███╗██╗███████╗██╗██╗  ██╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║██╔════╝██║╚██╗██╔╝
   ██║   █████╗  ██████╔╝██╔████╔██║██║█████╗  ██║ ╚███╔╝ 
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██╔══╝  ██║ ██╔██╗ 
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║     ██║██╔╝ ██╗
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝
"""
    print(Fore.MAGENTA + logo)
    print(Fore.MAGENTA + "                 TERMIFIX - Your Linux Terminal Assistant v1.0")
    print(Fore.MAGENTA + "                 Created by Yzeed Al Harthi\n")
    
    if system:
        print(Fore.MAGENTA + f"Available commands for {system}:")
        for i, cmd in enumerate(commands[system].keys(), start=1):
            print(Fore.MAGENTA + f"{i} - {cmd}")
        print(Fore.MAGENTA + "="*50)

# Choose action
print("Choose action:")
print("1 - Search error on Google")
print("2 - Run predefined command")

action = input("Enter number: ")

if action == "1":
    error_msg = input("Paste your error message: ")
    search_url = f"https://www.google.com/search?q={error_msg}"
    webbrowser.open(search_url)
    print("Search opened in your browser!")

elif action == "2":
    # Choose system
    print("\nChoose your system:")
    print("1 - Arch Linux")
    print("2 - Debian/Ubuntu")
    system_choice = input("Enter number: ")
    
    system = "arch" if system_choice == "1" else "debian"

    # Show banner + commands
    show_banner(system)
    system_commands = commands[system]

    # Choose command
    choice = input("\nEnter command number: ")
    try:
        choice = int(choice)
        cmd_key = list(system_commands.keys())[choice-1]
        command_to_run = system_commands[cmd_key]

        # Replace package placeholder
        if "<package_name>" in command_to_run:
            pkg_name = input("Enter package name: ")
            command_to_run = command_to_run.replace("<package_name>", pkg_name)

        print(f"Running: {command_to_run}")
        subprocess.run(command_to_run, shell=True)
    except:
        print("Invalid selection")

else:
    print("Invalid action")