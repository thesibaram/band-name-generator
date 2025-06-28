from colorama import init, Fore, Style
import cowsay as cs

"""
Band Name Generator
Author: Sibaram Behera

Generates a fun band name based on user input.
Styled using colorama for enhanced CLI experience.
"""

# Initialize colorama for colored text output
init(autoreset=True)

# Print a decorative header
print(Fore.CYAN + "="*50)
print(Fore.MAGENTA + Style.BRIGHT + "   🎸 Welcome to the Band Name Generator! 🎤   ")
print(Fore.CYAN + "="*50)

# Get user input for city and pet names
name = input(Fore.YELLOW + "What's the name of the city you grew up in: ").strip()
pets_name = input(Fore.YELLOW + "What's your pet's name: ").strip()

# Print the generated band name with styling

print(cs.cow(Fore.GREEN + Style.BRIGHT + f"Your band name is: {Fore.RED}{name.upper()} {pets_name.upper()}"))

# Print a decorative footer
print(Fore.CYAN + "="*50)
print(Fore.MAGENTA + Style.BRIGHT + "   Thanks for using the Band Name Generator!   ")
print(Fore.CYAN + "="*50)

