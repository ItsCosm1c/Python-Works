#Week 3 Homework
#Badge C3-1 (Else/If)
#Badge C3-2 (Boolean)
#Badge C3-3 (Comparisons)

password1 = input("Enter your password to get in: \n>").lower().strip()
password2 = input("Enter another password: \n>").lower().strip()        #(C3-3)nol

if(password1 == "knight" and password2 == "nolan"):             #(C3-1)
    print("You are now watching the movie 'The Dark Knight'.")
elif(password1 == "chamalet" and password2 == "zendaya"):       
    print("You are now watching the movie 'Dune Part 2'.")
elif(password1 == "morales" and password2 == "multiverse"):     #(C3-2)
    print("You are now watching the move 'Spiderman Across the Spiderverse'.")
else:
    print("You don't deserve to be here, get out.")