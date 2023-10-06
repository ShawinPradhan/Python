#function to calculate the area of triangle
def area_of_triangle(base,height):
    return 0.5 * base * height;

#Taking the base and height as input from the user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

#Printing the area of triangle
print(f"Area of triangle= ", area_of_triangle(base,height))

##OUTPUT
##Enter the base of the triangle: 5
##Enter the height of the triangle: 5
##Area of triangle=  12.5
