def open():
	
	HANGMAN_ASCII_ART= ("""
	  _    _                                         
	 | |  | |                                        
	 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
	 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
	 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
	 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
	                      __/ |                      
	                     |___/
	By - Amit Levy
	
	""")
	     
	MAX_TRIES = 6
	
	print (HANGMAN_ASCII_ART)
	print (MAX_TRIES , "Tries Left");
	

def check_word(secret_word):
	hidden_word = []
	for i in range(len(secret_word)):
		if secret_word[i] in alphabet:
			hidden_word.append("_")
		else:
			hidden_word.append(secret_word[i])
	return hidden_word

def show_hidden_word(hidden_word):
	word = ""
	for i in range(len(hidden_word)):
		word += hidden_word[i]
	print()
	print("Current Progress: ", word)


def check_valid_input(secret_word):
	num_of_tries = 0
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	letter_guessed = ""
	hidden_word = check_word(secret_word)
	game_over = False
	for i in range(5):
			print()
	print("    x-------x")
	for i in range(5):
			print()
	while not game_over:
		invalidInput = True
		while invalidInput:
			print("Player 2", end = "")
			letter_guessed = input(", please guess a letter: ").upper()
			if len(letter_guessed) > 1 or letter_guessed not in alphabet:
				print("You did enter a valid guess. Please try again.")
			else:
				invalidInput = False
				
		if letter_guessed in secret_word:
			for i in range(len(secret_word)):
				if secret_word[i] == letter_guessed:
					hidden_word[i] = letter_guessed
			show_hidden_word(hidden_word)
			if "_" not in hidden_word:
				print("Player 2 wins!")
				game_over = True
		else:
			num_of_tries += 1
			print("Your guess is incorrect! Please try again.")

			print("Hangman Status: ", end = "")
			
			if num_of_tries == 1:
				for i in range(5):
					print()
				print("""
    x-------x
    |
    |
    |
    |
    |
		""")
			elif num_of_tries == 2:
				for i in range(5):
					print()
				print("""
    x-------x
    |       |
    |       0
    |
    |
    |
		""")
			elif num_of_tries == 3:
				for i in range(5):
					print()
				print("""
    x-------x
    |       |
    |       0
    |       |
    |
    |
		""")
			elif num_of_tries == 4:
				for i in range(5):
					print()
				print("""
    x-------x
    |       |
    |       0
    |      -|-
    |
    |
		""")
			elif num_of_tries == 5:
				for i in range(5):
					print()
				print("""
    x-------x
    |       |
    |       0
    |      -|-
    |      - 
    |
		""")
			elif num_of_tries == 6:
				for i in range(4):
					print()
				print("-----  GAME OVER!   :(  -----")
				print("""
    x-------x
    |       |
    |       0
    |      -|-
    |      - -
    |
		""")
				
				game_over = True
			print("Number of chances left:", 6-num_of_tries)

			show_hidden_word(hidden_word)
							

def main():

	global alphabet
	secret_word = ""
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"		
	Continue = True
	open()
	
	print()
	secret_word = input("Player 1, please enter the secret word: ").upper()
	length = len(secret_word)
		
	for i in range(50):
		print()
		
	print ("_ "*length)

	print("Player 2, please guess the secret word")
	check_valid_input(secret_word)

	print()
	print("Goodbye!")

main()
