
def check_eligibility(age):
    eligible = "Eligible to vote" if age>=18 else "Not eligible to vote"
    return eligible;

try:
    age = int(input("Enter your age to check for voting eligibility: "))
    result = check_eligibility(age)
    print(result)
except ValueError:
    print("Please enter a valid age.")




