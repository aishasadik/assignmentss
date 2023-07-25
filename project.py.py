import random 
def generate_random_letter(): 
    return random.choice("abcdefghijklmnopqrstuvwxyz") 
def check_if_letters_in_same_group(letter1, letter2): return letter1 == letter2 
player1_name = input("What is your name, player ? ") 
player2_name = input("What is your name, player ? ") 
player1_letter = generate_random_letter() 
player2_letter = generate_random_letter() 
if check_if_letters_in_same_group(player1_letter, player2_letter): 
    print("You both have the same letter!") 
else: 
    print("You don't have the same letter.") 