#Week 5 Homework
#Badge C4-1 (While Loop)
#Badge C4-2 (For Loop)

hours_watched = 0

movies = {
        '1': "You are now watching Godzilla Minus One. What a fantastic movie.",
        '2': "You are now watching The Dark Knight. That is now my favorite superhero film.",
        '3': "You are now watching The Fugitive. This is now my favorite Harrison Ford film",
    }

while True:     #(Badge C4-1)
        print("Welcome to the movie collection. What movie do you want to see?")
        for key, description in movies.items():     #(Badge C4-2)
            print(f"Enter {key} to watch a movie.")

        print("Enter 0 to quit")

        choice = input("Choose a movie or exit: ")

        if choice in movies:
            print(movies[choice])
            hours_watched += 2
        elif choice == '0':
            print(f"Goodbye! You watched for {hours_watched} hours.")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 3.")
