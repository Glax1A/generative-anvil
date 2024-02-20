import itertools
import random
import sys

print("                                 _   _           \n                                | | (_)          \n  __ _  ___ _ __   ___ _ __ __ _| |_ ___   _____ \n / _` |/ _ \ '_ \ / _ \ '__/ _` | __| \ \ / / _ \\\n| (_| |  __/ | | |  __/ | | (_| | |_| |\ V /  __/\n \__, |\___|_| |_|\___|_|  \__,_|\__|_| \_/ \___|\n  __/ |                                          \n |___/ \n")
print("                  _ _ \n                 (_) |\n  __ _ _ ____   ___| |\n / _` | '_ \ \ / / | |\n| (_| | | | \ V /| | |\n \__,_|_| |_|\_/ |_|_|\n")
print("This tool is designed to take your wordlist and add them together, for example, lets say that your target is known for using DoB, names, etc in his password, just add that to a wordlist and this tool will develop that list into more passwords including symbols, and more. I do not condone any illegal activities.")
print(":::::::::::::::::::::::::::::::::::::::::::: \n:::::::::::::::::::::::::::::::::::::::::::: \n::::::::::::::::::::::::::::::::::::::::::::")
def substitute_lookalikes(word):
    substitutions = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5'}
    substituted_word = ''.join(substitutions.get(letter.lower(), letter) for letter in word)
    return substituted_word

def randomize_capitalization(word):
    return ''.join(random.choice([char.upper(), char.lower()]) for char in word)

def generate_wordlist(words_file, max_length, min_length, max_words, min_words, include_symbols, num_passwords, output_file, check_duplicates):
    with open(words_file, 'r') as file:
        words = [word.strip() for word in file.readlines() if min_length <= len(word.strip()) <= max_length]

    wordlist = []
    generated_phrases = set()
    num_generated = 0
    while num_passwords is None or num_generated < num_passwords:
        num_words = random.randint(min_words, max_words)
        word_subset = random.sample(words, num_words)
        phrase = ''.join(word_subset)
        if include_symbols:
            symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
            symbol_position = random.randint(0, len(phrase))
            symbol = random.choice(symbols)
            phrase = phrase[:symbol_position] + symbol + phrase[symbol_position:]
        
        # Check if duplicate checking is enabled and if the phrase is not a duplicate
        if not check_duplicates or phrase.lower() not in generated_phrases:
            substituted_phrase = substitute_lookalikes(phrase)
            wordlist.append(phrase)
            wordlist.append(substituted_phrase)
            wordlist.append(phrase.upper())
            wordlist.append(phrase.lower())
            
            # Generate all possible combinations of capitalization
            capital_combinations = [''.join(combination) for combination in itertools.product(*zip(phrase.upper(), phrase.lower()))]
            substituted_capital_combinations = [''.join(combination) for combination in itertools.product(*zip(substituted_phrase.upper(), substituted_phrase.lower()))]
            wordlist.extend(capital_combinations)
            wordlist.extend(substituted_capital_combinations)
            
            num_generated += 1
            if check_duplicates:
                generated_phrases.add(phrase.lower())

        # Exit loop if all possible combinations without duplicates have been generated
        if len(generated_phrases) == len(words) ** max_words:
            break

    if output_file:
        with open(output_file, 'w') as file:
            for item in wordlist:
                file.write("%s\n" % item)
        print(f"Wordlist saved to {output_file}")

        # Count the lines in the output file
        with open(output_file, 'r') as file:
            num_lines = sum(1 for line in file)

    print("                                 _   _           \n                                | | (_)          \n  __ _  ___ _ __   ___ _ __ __ _| |_ ___   _____ \n / _` |/ _ \ '_ \ / _ \ '__/ _` | __| \ \ / / _ \\\n| (_| |  __/ | | |  __/ | | (_| | |_| |\ V /  __/\n \__, |\___|_| |_|\___|_|  \__,_|\__|_| \_/ \___|\n  __/ |                                          \n |___/ \n")
    print("                  _ _ \n                 (_) |\n  __ _ _ ____   ___| |\n / _` | '_ \ \ / / | |\n| (_| | | | \ V /| | |\n \__,_|_| |_|\_/ |_|_|\n")
    print(f"Wordlist saved to {output_file}")

    print(f"Total number of passwords generated: {num_lines}")
    print(f"Remember that the duplicate checking system only half-works, so perhaps run another tool to remove duplicates!")
    print(f"Created by Nicholas M, Glax1A on Github.")
    return wordlist

def main():
    words_file = input("Enter the path to the file containing words (eg. /path/wordlist.txt): ")
    max_length = int(input("Enter the maximum character length for each outputted password: "))
    min_length = int(input("Enter the minimum character length for each outputted password: "))
    max_words = int(input("Enter the maximum number of words from the wordlist that can be used per outputted password: "))
    min_words = int(input("Enter the minimum number of words from the wordlist that can be used per outputted password: "))
    include_symbols = input("Include extra symbols in the phrases (Customizable inside the code)? (yes/no): ").lower() == 'yes'
    num_passwords = int(input("Enter the number of passwords to generate (or enter 0 for unlimited. Not fully working!): "))
    output_file = input("Enter the path to save the output file (eg. /path/newlist.txt. THIS WILL BE OVERWRITTEN): ")
    check_duplicates = input("Check for duplicate phrases (Not fully working)? (yes/no): ").lower() == 'yes'

    generate_wordlist(words_file, max_length, min_length, max_words, min_words, include_symbols, num_passwords, output_file, check_duplicates)

if __name__ == "__main__":
    main()
