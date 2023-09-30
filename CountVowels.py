#function to check whether the char is a vowel or not
def isVowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels

#taking input from the user
name = input("Enter a string to count the no. of vowels: ")

#count variable
count = 0

#iterating over each character in the string provided by the user
for char in name:
    if isVowel(char):
        #incrementing the count variable if the char is a vowel
        count += 1

#printing the no of vowels in the string
print("The no of vowels in the string: ",count)

##OUTPUT
##Enter a string to count the no. of vowels: Anudip
##The no of vowels in the string:  3
