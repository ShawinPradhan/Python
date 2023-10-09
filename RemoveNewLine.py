
#function to remove the new line from the string
def remove_newline(input_string):
    new_string = input_string.replace("\n","")
    return new_string

string = "\nBest \nDeeptech \nPython \nTraining\n"
clean_string = remove_newline(string)
print(clean_string)

##OUTPUT
##Best Deeptech Python Training
