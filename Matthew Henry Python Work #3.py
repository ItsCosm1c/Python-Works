password1 = input("Enter your password to get in: \n>").lower().strip()
password2 = input("Enter another password: \n>").lower().strip()    

if(password1 == "knight" or password2 == "nolan"): 
    print("You are now watching the movie 'The Dark Knight'.")
elif(password1 == "chamalet" or password2 == "zendaya"):       
    print("You are now watching the movie 'Dune Part 2'.")
elif(password1 == "morales" or password2 == "multiverse"): 
    print("You are now watching the move 'Spiderman Across the Spiderverse'.")
else:
    print("You don't deserve to be here, get out.")
