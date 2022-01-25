import numpy as np

dictionary_location = './english-words/words_alpha.txt'
wordle_word_length = 5

with open(dictionary_location) as word_file:
    english_words = list(set(word_file.read().split()))

five_letter_english_words = []
for word in english_words:
    if len(word) == wordle_word_length:
        five_letter_english_words.append(word)

five_letter_english_words.sort()

print("Example dictionary words: ", five_letter_english_words[:10])
print(dictionary_location, "DICTIONARY WORKING WELL... {} words loaded in memory.".format(len(five_letter_english_words)))

# print("robot" in five_letter_english_words)

def wordle_possibilities(word_required=None, unstable_required=None, verbosity=0):
    if not word_required:
        # Try default word. REMOVE THIS LATER AND ALSO ADD DOCSTRING.
        word_required = ['']*5

        #game-configuration (S=Stable letter letter_code[1], U=Unstable letters letter_code[1:]) (Can be anything and can be customised while making UI)
        word_required[0] = 'U'
        word_required[1] = 'So'
        word_required[2] = 'U'
        word_required[3] = 'U'
        word_required[4] = 'St'

        unstable_required = "rb"

    #find-possible-words
    matching_words = []

    for five_letter_english_word in five_letter_english_words:
        failed = False
        failing = True
        letters = unstable_required[:]  # Create a copy. letters will be changed.
        for i, letter_code in enumerate(word_required):
            if verbosity>=1:
                print("_________________________________________________________")
                print("Starting round for {}\t\t{}. Failed yet? {}".format(letter_code, five_letter_english_word, failed))
            if letter_code[0]=="S":
                if verbosity>=1:
                    print("Started S Processing...")
                
                letter = letter_code[1]
                
                if verbosity>=1:
                    print("Letter: {}".format(letter))
                    print(i, "letter_code was: {} word: {}".format(letter_code, five_letter_english_word))

                if five_letter_english_word[i] != letter:
                    failed = True
                    break
                #So, letter == required letter at this position. five_letter_english_word passing for now.
            elif letter_code[0]=="U":
                if verbosity>=1:
                    print("Started U Processing...", end=" ")
                if letters:
                    if verbosity>=1:
                        print("Letters Left: {}".format(letters))
                    letter_found = [False]*len(letters)
                else:
                    if verbosity>=1:
                        print("NO LETTERS LEFT! SKIPPING...")
                    continue
                    letter_found = []
                
                to_remove = []
                for j, letter in enumerate(letters):
                    if letter_found[j]==False:
                        if five_letter_english_word[i] == letter:
                            to_remove.append(j)
                            failing = False  # Shouldn't this be True instead?
                            letter_found[j] = True
                            break
                
                for j in to_remove:
                    letters = letters[:j-1]+letters[j+1:]

                if verbosity>=1:
                    print("letter_found, letters remaining, word:", letters, five_letter_english_word[i])        
                        
                if failing:
                    failed = True
                    break
                #So, letter == required possible letter at this position. five_letter_english_word passing for now.
            else:
                if verbosity>=1:
                    print("ERRRRRRRRRRRORRRR Make sure configuration is correctly defined in code above", letter_code)
        
        if not failed and len(letters)==0:
            if verbosity>=1:
                if five_letter_english_words:
                    print("WORDS SUPER LIKED YOU TODAY! Great Success --------------------------------> {}".format(five_letter_english_word))
                else:
                    print("SORRY! I can't find any word in my dictionary list that matches that configuration. Please try giving me a bigger dictionary list to ingest!")
            matching_words.append(five_letter_english_word)
            print(matching_words, "\n\n\n\n\n")
        
    print("ALRIGHT ALRIGHT> ALL DONE> POSSIBLE WORDS TO CHOOSE> \n\n", matching_words)
    return matching_words

# Getting configuration from the user

def play_wordle():
    print("""
Welcome to Worlde Bot. Please help me help you.

Here are the instructions:
You will be asked to enter a word configuration soon. Don't worry. Here's what it is.

"U" : Unknown Word
"S" : Known (Stable) Word

Known Words List : Letters that may fill up one of the unknown-word blanks. eg. "rb", "axc".

Example
-------
So, if we know that 
- The letters "r" and "b" are in a word. 
- "o" is definitely letter number 2 and 
- "t" is definitely letter number 5 then:

Then, 

Word Config will be : U So U U St (Unknown, Stable Letter "O", Unknown, Unknown, "Stable Letter "T")
""")
    verbosity = input("Please enter the verbosity you desire from the robot: ")

    while True:
        try:
            word_configuration = input("Enter Word Configuration : ").strip()
            if word_configuration.lower()=="exit":
                break
            unknown_variables = input("Enter Known Words List (eg: rbmx) : ")

            wordle_possibilities(word_configuration, unknown_variables, verbosity)
        except Exception as e:
            print("ERRRRRRRRRRRRRRRRRRRORRRRRRRRRRRRRRRRRRRRR", e)
            break
    
    print("Buh Byee")

if __name__ == "__main__":
    play_wordle()