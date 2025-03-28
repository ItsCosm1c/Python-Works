books = input('How many books did the student buy?\n>').lower().strip()

if(books == '0'):
    print("The student has earned 0 points.")
elif(books == '1'):
    print("The student has earned 5 points.")
elif(books == '2'):
    print("The student has earned 15 points.")
elif(books == '3'):
    print("The student has earned 30 points.")
elif(books >= '4'):
    print("The student has earned 60 points.")
