import itertools
import random

def substitute_lookalikes(word):
    substitutions = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5'}
    substituted_word = ''.join(substitutions.get(letter.lower(), letter) for letter in word)
    return substituted_word

def randomize_capitalization(word):
    return ''.join(random.choice([char.upper(), char.lower()]) for char in word)

def generate_wordlist(words_file, max_length=10, min_length=1, max_words=5, min_words=1, include_symbols=False, num_passwords=None, output_file=None, check_duplicates=True):
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


        # Count the lines in the output file
        with open(output_file, 'r') as file:
            num_lines = sum(1 for line in file)

    if output_file:
        with open(output_file, 'w') as file:
            for item in wordlist:
                file.write("%s\n" % item)
    print("                                 _   _           \n                                | | (_)          \n  __ _  ___ _ __   ___ _ __ __ _| |_ ___   _____ \n / _` |/ _ \ '_ \ / _ \ '__/ _` | __| \ \ / / _ \\\n| (_| |  __/ | | |  __/ | | (_| | |_| |\ V /  __/\n \__, |\___|_| |_|\___|_|  \__,_|\__|_| \_/ \___|\n  __/ |                                          \n |___/ \n")
    print("                  _ _ \n                 (_) |\n  __ _ _ ____   ___| |\n / _` | '_ \ \ / / | |\n| (_| | | | \ V /| | |\n \__,_|_| |_|\_/ |_|_|\n")
    print(f"Wordlist saved to {output_file}")

    print(f"Total number of passwords generated: {num_lines}")
    print(f"Remember that the duplicate checking system only half-works, so perhaps run another tool to remove duplicates!")
    print(f"Created by Nicholas M, Glax1A on Github.")

    return wordlist


# Example usage:
generate_wordlist(
    # Where to take the words for messing around with from:
    'wordlist.txt',
    # Maximum length of the outputted stuff
                  max_length=9,
                  # Minimum length of outputted stuff
                  min_length=4,
                  # Maximum words from the wordlist that can be used per outputted password
                  max_words=2,
                  # Minimum words from wordlist per password
                  min_words=1,
                  include_symbols=False,
                  num_passwords=111,
                  output_file='newlist.txt',
                  check_duplicates=True)

# Checking for duplicates is more resource intensive, and keeps missing duplicates, do tell me if you know y! Not using it will definitely get you a file at least double the size, tho. Use with caution.
# Symbols are randomly placed throughout the output and may prove useless, I just disable them when I use.
# Setting the number of pass to generate to the value of none will mean it generates infinitely. Or at least thats meant to be the case, again, please do tell me y!!!