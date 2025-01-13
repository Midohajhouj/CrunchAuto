## Crunch Automated

This tool is a customizable wordlist generator that allows you to generate wordlists based on a custom set of characters. You can specify the minimum and maximum lengths for the generated words, add a prefix or suffix, and save the result to a file. This tool is perfect for penetration testers and security researchers who need to generate wordlists for brute-force attacks, password cracking, or any other purpose.

## Features

- **Custom Character Set**: Generate wordlists from a custom set of characters (e.g., letters, numbers, special characters).
- **Length Control**: Specify the minimum and maximum lengths for the generated words.
- **Prefix and Suffix**: Add a custom prefix and/or suffix to each generated word.
- **Append Mode**: Option to append to an existing wordlist file or overwrite it.
- **Wizard Mode**: Interactive mode that guides you step by step through configuring the wordlist generation.
- **Preview Mode**: View a preview of the generated wordlist before finalizing.

## Prerequisites

Before using this tool, ensure that the following Python modules are installed:

- **Python 3.x**: Ensure you have Python 3.x installed. You can check by running:
  
  ```bash
  python --version

    colorama: This script uses the colorama library to provide colorful output. Install it using:

    pip install colorama

    itertools: This is part of Python's standard library, so no installation is needed.

Installation

    Clone the repository or download the script:

git clone 
cd CrunchAuto

Make sure you have the required Python dependencies installed:

pip install colorama

Now, you can run the script using Python:

    python crunch.py

    
Usage

You can use this script in two modes: Wizard Mode for step-by-step interaction or Command-Line Mode for direct execution.
Basic Usage (Command-Line Mode)

To generate a wordlist, simply call the script with the necessary arguments.

python crunch.py -c "abc" -min 3 -max 5 -o wordlist.txt

This will generate a wordlist with words of length 3 to 5 using the characters "abc" and save the output in wordlist.txt.
Wizard Mode

You can also use the Wizard Mode, which will guide you through the configuration process interactively.

python crunch.py -w

This will prompt you for:

    Characters to use for the wordlist.
    Minimum and maximum lengths for the words.
    Output file name.
    Whether to append to an existing file.
    A prefix and suffix to prepend or append to each word.

Example Usage

Generate wordlist with a custom character set:

python crunch.py-c "abc123" -min 4 -max 6 -o wordlist.txt

Generate wordlist with a prefix:

python crunch.py -c "xyz" -min 3 -max 5 -o wordlist.txt -pfx "test_"

Generate wordlist with a suffix:

python crunch.py -c "1234" -min 2 -max 4 -o wordlist.txt -s "_suffix"

Help

To view all available options and how to use them, run:

python crunch.py -h

Output Format

The script generates a wordlist that will be saved to the specified output file. If you choose to preview the output, the first few lines will be displayed in the terminal.

Example output:

test_abc
test_abd
test_abe
...

Troubleshooting
Python Not Installed

If you receive an error indicating that Python is not found, make sure that Python 3.x is installed. On Linux-based systems, you can install Python using:

sudo apt-get install python3  # Ubuntu/Debian
sudo yum install python3      # CentOS/RHEL

On macOS, use Homebrew:

brew install python3

colorama Not Installed

If you receive an error regarding the missing colorama library, install it using:

pip install colorama

Contributing

Feel free to open issues or submit pull requests if you have suggestions, bug fixes, or improvements. Contributions are welcome!
License

This project is open-source and released under the MIT License. See the LICENSE file for more details.
Contact

If you have any questions or need further assistance, feel free to contact the author at:

    Email: midohajhouj11@example.com
    GitHub: https://github.com/Midohajhouj


This README provides an overview of the Wordlist Generator tool, including installation, usage, and troubleshooting steps. You can modify it further to suit the specifics of your project.