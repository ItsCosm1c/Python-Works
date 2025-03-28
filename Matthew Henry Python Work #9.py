#Week 8 Homework
#badge C5-4 (Scope)
#Badge C6-1 (Try/Except)
#Badge C6-2 (Read or Write Data)


def sum_odd_lines(filename):
    def calculate_sum():
        try: #(C6-1)
            with open(filename, 'r') as file:
                total = 0
                for index, line in enumerate(file, start=1):
                    try:
                        if index % 2 != 0:
                            total += int(line.strip())
                    except ValueError:
                        print(f"Warning: Could not convert line {index} to an integer. Skipping it.")
            
            print(f"The sum of numbers on odd lines is: {total}")
        
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
    
    calculate_sum() #(C5-4) this is the scope function in the code

sum_odd_lines('numbers.txt') #(C6-2) this is the part where the code reads the number.txt file
