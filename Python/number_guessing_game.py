import random
play_game="yes"
while play_game.lower()!="no":
    def difficulty_level():
        while True:
            try:
                print("Choose your difficulty level:")
                print("1. Easy(10 attempts)")
                print("2. Medium(7 attempts)")
                print("3. Hard(5 attempts)")
                difficulty=int(input("Enter your choice:"))
            except ValueError:
                print("Invalid input! Please enter a valid option.")
                continue
            if difficulty==1:
                return 10
            elif difficulty==2:
                return 7
            elif difficulty==3:
                return 5
            else:
                print("Invalid choice! Enter a valid option.")


    print("WELCOME TO THE NUMBER GUESSING GAME!")
    num=random.randint(1,100)
    max_attempts=difficulty_level()
    game_over=False
    guess=1
    while not game_over and guess<=max_attempts:
        try:
            guess_num=int(input("Guess the number between 1 and 100:"))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        if guess_num < 1 or guess_num > 100:
            print("Please enter a number between 1 and 100.")
            continue
        if guess_num<num:
            print("Too low")
            guess+=1
        elif guess_num>num:
            print("Too high")
            guess+=1
        else:
            print("YOU WON THE GAME!")
            print("You guessed it in",guess,"guesses")
            game_over=True
    if game_over==False:
        print("YOU LOST THE GAME! The number was",num)
    while True:
        play_game = input("Do you want to play again? (yes/no): ").lower()

        if play_game == "yes" or play_game == "no":
            break
        else:
            print("Invalid choice! Please enter yes or no.")