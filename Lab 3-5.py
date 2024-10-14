# Christian Ocampo 10/13/2024 Lab 3 module


miles_driven =float(input("Enter the number of miles driven:"))

gallons_used = float(input("enter the number of gallons used:"))

mpg = miles_driven / gallons_used

print(f"You drove {miles_driven} miles using {gallons_used} gallons")
print(f"Wow! Your car was able to take you that far, you have a great car! {mpg: .2f} miles per gallon (MPG).")