#function to check whether a person is eligible to vote or not
def check_eligibility(age):
    eligible = "Eligible to vote" if age>=18 else "Not eligible to vote"
    return eligible;

try:
    #Taking age as input fro the user
    age = int(input("Enter your age to check for voting eligibility: "))
    result = check_eligibility(age)
    print(result)
#handling the ValueError exception
except ValueError:
    print("Please enter a valid age.")

# OUTPUT
# Enter your age to check for voting eligibility: 18
# Eligible to vote


