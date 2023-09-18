#1. display the sum of even numbers less than 8
#2. input 5 numbers from the keyboard and find their average
#3. print the output of the following
#a) -5+8*6
#b) (55+6)%9
#c) 20+-3*5/8
#d) 5+15/3*2-8%3
#4. store an arraylist of animals and print them


#1. 
# Initialize a variable to store the sum
sum_of_evens = 0

# Loop through numbers
for num in range(2, 8, 2):
    sum_of_evens += num

# Display the sum
print("Sum of even numbers less than 8:", sum_of_evens)

#2. 
# store the sum
total = 0

# Loop to input 5 numbers
for i in range(5):
    # get user input 
    num = float(input("Enter a number: "))
    
    # Add it to the total
    total += num

# Calculate the average
average = total / 5

# Display the average
print("Average of the 5 numbers:", average)

#3. a)
result = -5 + 8 * 6
print(result)

#b)
result2 = (55+6)%9
print(result2)

#c)
result3 = 20+-3*5/8
print(result3)

#d)
result4 = 5+15/3*2-8%3
print(result4)

#4. 
# Create a list of animals
animals = ["Dog", "Cat", "Elephant", "Lion", "Giraffe"]

# Iterate through the list and print each animal
print("List of animals:")
for animal in animals:
    print(animal)

#5. 