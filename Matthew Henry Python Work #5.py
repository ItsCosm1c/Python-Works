hours_watched = 0

while True: 
        print("Welcome to the movie collection. What movie do you want to see?")
        for x in [1,2,3]: 
            print(f"Enter {x} to watch a movie.")

        print("Enter 0 to quit")

        choice = input("Choose a movie or exit: ")

        hours_watched += 2
            
        if int(choice) == 1:
             print(f"You are now watching Godzilla Minus One. The best Godzilla movie!")
        elif int(choice) == 2:
             print(f"You are now watching Dune Part 2. Best movie that has come out this year!")
        elif int(choice) == 3:
             print(f"You are now watching The Fugitive. The best Harrison Ford film to date.")
        elif choice == '0':
            hours_watched -= 2
            print(f"Goodbye! You watched for {hours_watched} hours.")
            break
        else:
          hours_watched -=2
          print("Invalid choice. Please enter a number between 0 and 3.")
          
