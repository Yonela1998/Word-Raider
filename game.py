import random

def reading_from_txt():
    with open("words.txt","r",errors='ignore') as file:
        contents = file.readlines()
        words_list = []
        for line in contents:
            words_list.append(line.strip())
        return words_list
    
def random_word():
    words_list = reading_from_txt()
    word = random.choice(words_list)
    return word
    
    

if __name__ == "__main__":
    
    word = random_word()
    incorrect_guess = []
    misplaced_guess = []
    output = ["_","_","_","_","_"]
    current_turns = 0
    max_turns = 5
    
    print("Welcome to the Word Guessing Game! 🎉","\n\nPut your thinking caps on and get ready to have some fun!")
    print("Your goal is to guess the hidden 5-letter word by suggesting words.")
    print("With each correct guess, you’ll get closer to solving the puzzle, but watch out for wrong guesses—they could lead to your downfall!\n")
    print("You only have 5 tries to guess the word.\nAre you ready to test your vocabulary and have a blast? Let’s get started! Good luck! 🍀✨\n")    
    
    
    
    for i in range(max_turns):
        while True:
            user_guess = input("Please enter your guess: ")
            if len(user_guess) == 5:
                break
        
        user_guess = user_guess.lower()
        for i in range(len(user_guess)):
            if user_guess[i] == word[i]:
                output[i] = user_guess[i]
            elif user_guess[i] in word and user_guess[i] not in misplaced_guess:
                misplaced_guess.append(user_guess[i])
            elif user_guess[i] not in incorrect_guess:
                incorrect_guess.append(user_guess[i])
        
        if "_" in output:       
            print(output)
            print("Misplaced letters are: ",misplaced_guess)
            print("Incorect letter guesses are: ",incorrect_guess)
            print("\n")
        else:
            print(f"Congrats🎉🎉🎉 You did it!\nYou've correctly guessed {word}.")
            break
            
            
            