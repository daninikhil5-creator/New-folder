import random
def game():
    level = input("which level do you prefer in game(easy,medium,hard) :").lower()
    try:
        if level == "easy":
            guessed_value = random.randint(1,50)
            file1 = open("easy.score.txt","r+")
            name_file2 = "easy.high.score.txt"
    
        elif level == "medium":
            guessed_value = random.randint(1,100)
            file1 = open("medium.score.txt","r+")
            name_file2 = "medium.high.score.txt"
    
    
        elif level == "hard":
            guessed_value = random.randint(1,500)
            file1 = open("hard.score.txt","r+")
            name_file2 = "hard.high.score.txt"


        else:
            return

        attempt = 0
        while True:
            number = int(input("enter the number :"))
            attempt+=1
            if number == guessed_value:
                print(f"you've guess the number {guessed_value} in {attempt} attempts")
                break
            elif number<guessed_value:
                print(f"this is too small, try greater number")

            elif(number>guessed_value):
                print(f"this is too greater, try smaller number")
        
        file1.write(f"{attempt}")
        file1.seek(0)
        data = file1.read()
        print(f"your score:{data}")
        highscore = open(name_file2,"r+")
        high = highscore.readline()
        try:
            if int(data) < int(high):
                highscore.seek(0)
                highscore.write(data) 
    
            print(f"high score:{high}")
        except Exception as e:
            highscore.seek(0)
            highscore.write(data)
            highscore.seek(0)
            print(f"high score:{high}")
        

        highscore.close()
        file1.close()
    
    except Exception as f:
        print("enter only easy,medium or hard")
    


    play_again = input("do you want to play again.(yes/no):").lower()
    
    if play_again=="yes":
        game()
    else:
        pass

game()
