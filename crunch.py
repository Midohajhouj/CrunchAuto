import itertools
import argparse
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def display_banner():
    """
    Displays a colorful banner for the script.
    """
    banner = f"""
    {Fore.CYAN}================================
       {Fore.YELLOW} Crunch Automated
    {Fore.CYAN}================================
    {Fore.GREEN}Generate a wordlist from your 
    custom character set with ease!
    {Fore.MAGENTA}Edited by: MIDO
    """
    print(banner)

def generate_wordlist(characters, min_length, max_length, output_file, append=False, prefix="", suffix=""):
    """
    Generates a wordlist of all possible combinations of characters with an optional prefix and suffix.

    Args:
        characters (str): The characters to use for generating combinations.
        min_length (int): The minimum length of combinations.
        max_length (int): The maximum length of combinations.
        output_file (str): The file to save the wordlist.
        append (bool): Whether to append to the file (default: False).
        prefix (str): The prefix to prepend to each combination (default: empty string).
        suffix (str): The suffix to append to each combination (default: empty string).
    """
    mode = 'a' if append else 'w'
    try:
        with open(output_file, mode) as f:
            for length in range(min_length, max_length + 1):
                for combination in itertools.product(characters, repeat=length):
                    word = prefix + ''.join(combination) + suffix  # Using prefix and suffix here
                    f.write(word + '\n')
        print(f"{Fore.GREEN}Wordlist successfully generated in '{output_file}'")
    except IOError as e:
        print(f"{Fore.RED}An error occurred while writing to the file: {e}")

def preview_wordlist(output_file, lines=10):
    """
    Previews the first few lines of the generated wordlist.

    Args:
        output_file (str): The file to preview.
        lines (int): Number of lines to preview (default: 10).
    """
    try:
        print(f"{Fore.CYAN}Previewing the first {lines} lines of '{output_file}':")
        with open(output_file, 'r') as f:
            for i, line in enumerate(f):
                if i >= lines:
                    break
                print(f"{Fore.YELLOW}{line.strip()}")
    except IOError as e:
        print(f"{Fore.RED}An error occurred while reading the file: {e}")

def wizard_mode():
    """
    Wizard mode for interactive step-by-step input.
    """
    print(f"{Fore.CYAN}Welcome to Wizard Mode! Follow the prompts to configure the wordlist generator.")
    try:
        # Step 1: Get characters
        characters = input(f"{Fore.CYAN}Enter the characters to use (e.g., abc): {Fore.RESET}").strip()
        if not characters:
            raise ValueError("You must provide at least one character.")
        
        # Step 2: Get minimum and maximum word lengths
        min_length = int(input(f"{Fore.CYAN}Enter the minimum word length: {Fore.RESET}"))
        max_length = int(input(f"{Fore.CYAN}Enter the maximum word length: {Fore.RESET}"))
        if min_length <= 0 or max_length <= 0 or min_length > max_length:
            raise ValueError("Invalid length values provided.")
        
        # Step 3: Get output file name
        output_file = input(f"{Fore.CYAN}Enter the output file name (e.g., wordlist.txt): {Fore.RESET}").strip()
        if not output_file:
            raise ValueError("Output file name cannot be empty.")
        
        # Step 4: Append mode
        append_mode = input(f"{Fore.CYAN}Do you want to append to the file if it exists? (yes/no): {Fore.RESET}").strip().lower() == 'yes'
        
        # Step 5: Get prefix
        prefix = input(f"{Fore.CYAN}Enter a prefix to prepend to each word (default: none): {Fore.RESET}").strip()
        
        # Step 6: Get suffix
        suffix = input(f"{Fore.CYAN}Enter a suffix to append to each word (default: none): {Fore.RESET}").strip()
        
        # Step 7: Confirm settings
        print(f"\n{Fore.GREEN}Settings:")
        print(f"{Fore.YELLOW}Characters: {characters}")
        print(f"{Fore.YELLOW}Min Length: {min_length}")
        print(f"{Fore.YELLOW}Max Length: {max_length}")
        print(f"{Fore.YELLOW}Output File: {output_file}")
        print(f"{Fore.YELLOW}Append Mode: {'Yes' if append_mode else 'No'}")
        print(f"{Fore.YELLOW}Prefix: {prefix if prefix else '(None)'}")
        print(f"{Fore.YELLOW}Suffix: {suffix if suffix else '(None)'}")
        
        confirm = input(f"\n{Fore.CYAN}Do you want to proceed? (yes/no): {Fore.RESET}").strip().lower()
        if confirm != 'yes':
            print(f"{Fore.RED}Wizard mode canceled. Exiting...")
            return

        # Generate the wordlist
        generate_wordlist(characters, min_length, max_length, output_file, append=append_mode, prefix=prefix, suffix=suffix)

        # Step 8: Preview
        preview_choice = input(f"{Fore.CYAN}Would you like to preview the generated wordlist? (yes/no): {Fore.RESET}").strip().lower()
        if preview_choice == 'yes':
            preview_wordlist(output_file)
    except ValueError as e:
        print(f"{Fore.RED}Input error: {e}")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Display the banner
    display_banner()

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a wordlist from custom character sets.")
    parser.add_argument("-c", "--characters", help="Characters to use for generating the wordlist (e.g., 'abc').")
    parser.add_argument("-min", "--min-length", type=int, help="Minimum length of the words.")
    parser.add_argument("-max", "--max-length", type=int, help="Maximum length of the words.")
    parser.add_argument("-o", "--output-file", help="Output file name (e.g., 'wordlist.txt').")
    parser.add_argument("-a", "--append", action="store_true", help="Append to the output file instead of overwriting it.")
    parser.add_argument("-p", "--preview", type=int, nargs='?', const=10, help="Preview the first N lines of the wordlist (default: 10).")
    parser.add_argument("-pfx", "--prefix", help="Prefix to prepend to each word (default: none).")
    parser.add_argument("-sfx", "--suffix", help="Suffix to append to each word (default: none).")
    parser.add_argument("-w", "--wizard", action="store_true", help="Run the script in wizard mode for step-by-step input.")
    
    args = parser.parse_args()

    if args.wizard:
        # Run in wizard mode
        wizard_mode()
    else:
        # Ensure required arguments are provided
        if not all([args.characters, args.min_length, args.max_length, args.output_file]):
            print(f"{Fore.RED}Error: Missing required arguments. Use -h for help or run in wizard mode (-w).")
        else:
            try:
                # Generate the wordlist
                generate_wordlist(
                    characters=args.characters,
                    min_length=args.min_length,
                    max_length=args.max_length,
                    output_file=args.output_file,
                    append=args.append,
                    prefix=args.prefix or "",
                    suffix=args.suffix or ""  # Add suffix if provided
                )

                # Preview the wordlist if requested
                if args.preview is not None:
                    preview_wordlist(args.output_file, lines=args.preview)
            except Exception as e:
                print(f"{Fore.RED}An unexpected error occurred: {e}")

