
#fucntion to reverse a string
def reverse_string(input_string):

    #splitting the words
    words = input_string.split()

    #reversing the order of the words
    reversed_words = words[::-1]

    #joining the words again with whitespace between them
    reversed_string = ' '.join(reversed_words)

    return reversed_string

String = "Deeptech Python Training"
print(reverse_string(String))

##OUTPUT
##Training Python Deeptech
