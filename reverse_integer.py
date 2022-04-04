# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

#-592 --> -295
#1099 --> 9901
#123 --> 321

# 25.704 --> 407.52 

# 25- --> -52

# 2A5 --> 5A2

#600 --> 006 --> 6

def reverse_integer(num):
    num = str(num)

    #check if the input is valid ? if not return error message
    if num.replace('-','').isdigit() == False:
        print("The input was not a valid integer.")
        return

    rev_num = []

    #loop through each character and insert at beginning of array
    for char in num:
        rev_num.insert(0, char)

    #negative sign at the end? move it to the front!
    if rev_num[len(num)-1] == "-":
        rev_num.pop()
        rev_num.insert(0, "-")

    #join the array and print + return the solution
    solution = "".join(rev_num)
    print(int(solution))
    return(int(solution))


reverse_integer('2a5')