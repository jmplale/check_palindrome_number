# let's make a def function
def palindrome(number):
    reverse = int(str(number)[::-1]) # make this to check if the reverse of char is stil the same
    #if statement
    if number == reverse:
        print(f"original number {number}")
        print("Yes. given number is palindrome number")
        return True
    # else statement
    else:
        print(f"original number {number}")
        print("No. given number is not palindrome number")
        return False

# test the program
palindrome(121)
print("")
palindrome(125)