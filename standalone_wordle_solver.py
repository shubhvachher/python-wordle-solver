import numpy as np

dictionary_location = './english-words/five_letter_english_words.txt'
wordle_word_length = 5

with open(dictionary_location) as word_file:
    english_words = list(set(word_file.read().split()))

five_letter_english_words = []
for word in english_words:
    if len(word) == wordle_word_length:
        five_letter_english_words.append(word)

five_letter_english_words.sort()

print("Example dictionary words: ", five_letter_english_words[:10])
print(dictionary_location, "DICTIONARY WORKING WELL... {} five letter english words loaded in memory.".format(len(five_letter_english_words)))

# print("robot" in five_letter_english_words)

def wordle_possibilities(word_required=None, unstable_required=None, known_impossibles=None, verbosity=0):
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

        known_impossibles = "xf"
    
    if isinstance(word_required, str):
        final_word_configuration = []
        i = 0
        while i < len(word_required):
            if word_required[i]=="U":
                final_word_configuration.append("U")
            elif word_required[i]=="S":
                final_word_configuration.append("S"+word_required[i+1])
                i += 1
            else:
                raise("THIS IS AN INVALID ENTRY. READ INSTRUCTIONS.")
            
            i += 1

        word_required = final_word_configuration

    matching_words = []

    for five_letter_english_word in five_letter_english_words:
        failed = False
        failing = True
        letters_required = unstable_required[:]  # Create a copy. letters will be changed.
    
        for i, letter_code in enumerate(word_required):
            
            if verbosity>=1:
                print("_________________________________________________________")
                print("Starting round for {}\t\t{}. Failed yet? {}".format(letter_code, five_letter_english_word, failed))
            
            if letter_code[0]=="S":
                
                letter = letter_code[1]
                
                if five_letter_english_word[i] != letter:
    
                    if verbosity>=1:
                        print("{} is not {}. So, FAILED.".format(five_letter_english_word[i], letter))
    
                    failed = True
                    break
                #So, letter == required letter at this position. five_letter_english_word passing for now.
            
            elif letter_code[0]=="U":
                if five_letter_english_word[i] in known_impossibles:

                    if verbosity>=1:
                        print("{} found! So, FAILED.".format(five_letter_english_word[i]))

                    failed = True
                    break

                if five_letter_english_word[i] in letters_required:
                    letters_required = letters_required.replace(five_letter_english_word[i], "")

                    if verbosity>=1:
                        print("Found {} and new required letters list is {}".format(five_letter_english_word[i], letters_required))
            else:
                if verbosity>=1:
                    print("ERRRRRRRRRRRORRRR Make sure configuration is correctly defined in code above", letter_code)
        
        if not failed and len(letters_required)==0:
            if verbosity>=1:
                print("WORD FOUND! Great Success --------------------------------> {}".format(five_letter_english_word))
     
            matching_words.append(five_letter_english_word)
      
            if verbosity>=2:
                print(matching_words, "\n\n\n\n\n")
        
    print("ALRIGHT ALRIGHT... ALL DONE! WORDS THAT SUPER LIKED YOU TODAY ---> \n\n", matching_words)
    return matching_words

# Getting configuration from the user

def play_wordle():
    
    print("""

Welcome to Worlde Bot. Please help me help you.

Here are the instructions:
You will be asked to enter a word configuration soon. Don't worry. Here's how it's done.

"U" : Unknown Word
"S" : Known (Stable) Word

So, if we know that 
- "o" IS definitely letter number 2 
- "t" IS definitely letter number 5
- "r" and "b" are there somewhere in the word
- "b", "x" and "f" are NOT in the word

Then, 

Word Config will be : U So U U St (without spaces, with "U" and "S" upper case and actual letters lower case: like : "USoUUSt") (Unknown, Stable Letter "o", Unknown, Unknown, "Stable Letter "t")

And Known Letters List (yellow letters) : Letters that may fill up one of the unknown-word blanks. eg. input: "rb"

And Known Impossibilities List (grey letters) : Letters that are not there in the word. eg. "acyz"
___________________________________________________________________________________________________________________________________
""")

    # verbosity = int(input("Please enter the VERBOSITY you desire from the robot: "))
    verbosity = 0  # Use the notebook if you'd like more verbosity, to see how the code works

    while True:
        try:
            word_configuration = input("\n\n\n START! Enter Word Configuration (without spaces) : ").strip()
            if word_configuration.lower()=="exit":
                break
                # raise()

            
            final_word_configuration = []
            i = 0
            while i < len(word_configuration):
                if word_configuration[i]=="U":
                    final_word_configuration.append("U")
                elif word_configuration[i]=="S":
                    final_word_configuration.append("S"+word_configuration[i+1])
                    i += 1
                else:
                    raise("THIS IS AN INVALID ENTRY. READ INSTRUCTIONS.")
                
                i += 1
                
            unknown_variables = input("Enter Known Letters (without spaces) : ")

            known_impossibles = input("Enter Known Impossibles (without spaces) : ")

            print("Starting the Algorithm with inputs: {}, {}, {} and verbosity {}".format          (final_word_configuration, 
                                unknown_variables,
                                known_impossibles,
                                verbosity))

            wordle_possibilities(final_word_configuration, unknown_variables, known_impossibles, verbosity)
        except Exception as e:
            print("ERRRRRRRRRRRRRRRRRRRORRRRRRRRRRRRRRRRRRRRR", e.message())
            break
    
    print("Buh Byee")

if __name__ == "__main__":
    play_wordle()