"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Mykola Tikhonov
email: mykola.tikhonov@seznam.cz
discord: phranschyze
"""

from task_template import TEXTS

username = input("Please enter your username: ")
password = input("Please enter your password: ")

# list of objects - registered users
registered_users = {
    'bob': "123", 
    'ann': "pass123",
    'mike': "password123",
    'liz': "pass123"
}

# zacatek IF funkce + 2x rozdelovac
if username in registered_users and password == registered_users[username]:
    print("-" * 23, "Welcome to the app " + str(username), "We have 3 texts to be analyzed.", "-" * 23, sep="\n")
    
    # ošetření uživatelského vstupu pro výběr textu
    try:
        select_text = int(input("Please select text to analyze (1, 2 or 3): "))
        if select_text < 1 or select_text > 3:
            print("Invalid selection, please choose a text between 1 and 3.")
            exit()
        selected_text = TEXTS[select_text - 1]
    except ValueError:
        print("Invalid input, please enter a number (1, 2, or 3).")
        exit()
    
    # split slov ve vybranem analyzovanem textu a odstranění nežádoucích znaků
    words = [word.strip(".,!?") for word in selected_text.split()]

    # Inicializace statistik
    total_words = len(words)
    title_case_words = 0
    upper_case_words = 0
    lower_case_words = 0
    numeric_words = 0
    total_numbers_sum = 0
    word_lengths = {}

    # Jedna smyčka pro všechny statistiky
    for word in words:
        if word.istitle():
            title_case_words += 1
        if word.isupper() and word.isalpha():  # Písmena pouze v uppercase, čímž vyloučíme např. 30N
            upper_case_words += 1
        if word.islower():
            lower_case_words += 1
        if word.isdigit():  # Pouze čísla, vylučuje kombinace jako 30N
            numeric_words += 1
            total_numbers_sum += int(word)
        
        word_len = len(word)
        if word_len in word_lengths:
            word_lengths[word_len] += 1
        else:
            word_lengths[word_len] = 1

    # Výpis statistik
    print("-" * 23, f"Number of words in the selected text: {total_words}", sep="\n")
    print(f"Number of words in the selected text starting with a capital letter: {title_case_words}")
    print(f"Number of words in the selected text written with all capital letters: {upper_case_words}")
    print(f"Number of words in the selected text written with lower letters: {lower_case_words}")
    print(f"Number of words in the selected text which are numbers: {numeric_words}")
    print("-" * 45, f"Total sum of numbers in selected text: {total_numbers_sum}", "-" * 45, sep="\n")

    # Sloupcový graf
    print(f"{'LEN|':<4}{'OCCURRENCES':^20}{'|NR.':>6}")
    print("-" * 32)
    for length in sorted(word_lengths):
        count = word_lengths[length]
        print(f"{length:<4}{('*' * count):<20}{count:>6}")

# zbytek IF funkce
else:
    print("You're not authorized, terminating program...")
