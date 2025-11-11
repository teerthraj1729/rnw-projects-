print("Welcome to the Interactive Personal Data Collector")

name= str(input("Please enter your name:  "))
age= int(input("Please enter your age : " ))
height= float(input("Please enter your height in meters: "))
hobby= str(input("Please enter your hobby : "))

print("Thank you! Here is the infromation we collected:" )

print("Name :",name,"and" , "its type is: ", type(name),"and" ," memory address is: ",id(name))
print("Age :",age,"and" , "its type is: ", type(age),"and" ," memory address is: ",id(age))
print("Height :",height,"and" , "its type is: ", type(height),"and" ," memory address is: ",id(height))
print("Hobby :",hobby,"and" , "its type is: ", type(hobby),"and" ," memory address is: ",id(hobby))
current_year= 2025
year=(current_year-age)
 

print("Your birth year is approximately:",year,"(based on your age)",age )

print("Thank you for using the Personal Data Collector. Goodbye!")
