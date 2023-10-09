
#function to check whether an input string is palindrome or not
def is_palindrome(input_string):
    start = 0
    end = len(input_string) - 1

    #removing case censitivity by changing the string to lower_case
    input_string= input_string.lower()
    
    for _ in range(len(input_string) // 2):
        if input_string[start] != input_string[end]:
            return False

        #incremeting and decrementing the start and end index respectively
        start += 1
        end -= 1

    return True

#taking user input
user_input = input("Please enter a string: ")

#checking if the user input is palindrome or not
if is_palindrome(user_input):
    print("The string is palindrome.",user_input)
else:
    print("The string is not palindrome.",user_input)

'''
OUTPUT
Please enter a string: Eagle
The string is not palindrome. Eagle

Please enter a string: Madam
The string is palindrome. Madam  '''
