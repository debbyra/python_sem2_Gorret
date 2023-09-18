#1. sum of items in alist
#2a). write a function that takes 2lists and returns true if they have one common member
#b). append a new member 55
#c) replace a member

#1. 
# Create a list of numbers
alist = [1, 2, 3, 4, 5]

# Calculate the sum of the items in the list
total = sum(alist)

# Print the result
print("Sum of items in the list:", total)


#2.a)
def common_member(list1, list2):
    # Convert the lists to sets for efficient intersection check
    set1 = set(list1)
    set2 = set(list2)
    
    # Check if there is any common element
    common_elements = set1.intersection(set2)
    
    # If there are common elements, return True; otherwise, return False
    return bool(common_elements)

# Example:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = common_member(list1, list2)
print("Do the lists have a common member?", result)

#b) 
# Append the new member (55) to the list
list1.append(55)

# Print the updated list
print(list1)

#c)
# Index of the element you want to replace 
index_to_replace = 2  

# New value to replace the existing element
new_value = 22

# Replace the element at the specified index with the new value
list2[index_to_replace] = new_value

# Print the updated list
print(list2)


