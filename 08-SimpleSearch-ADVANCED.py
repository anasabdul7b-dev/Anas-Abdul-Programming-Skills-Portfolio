# EXERCISE 8 - Simple Search (With BONUS)

list = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] # List of names to search through

# Display objective and the list of names
print("\nOBJECTIVE: Identify the target in the list of names.")
print("Name List:", list)

# Convert all names to lowercase for case-insensitive search
list_lower = [name.lower() for name in list]

# Loop until the user finds the target
while True:
    search = input("\nEnter the name you want to search for: ") # Ask the user which name they want to search
    search_lower = search.lower() # Convert input to lowercase

    # Check if the input is in the list (case-insensitive)
    if search_lower in list_lower:
        name_found = list[list_lower.index(search_lower)] # Retrieve the original name with correct capitalization

        # Special target: "Sam"
        if search_lower == "sam":
            print(f'{name_found} was found in the list, This is the person we are looking for!')
            break # Exit loop after finding the target
        else:
            print(f'{name_found} was found in the list, but this is not the target. Keep searching!') # Name is in list but not the target
    else:
        print(f'{search} is NOT in the list. Try a name from the list.') # Name is not in the list

print("\nSearch Complete! You successfully found the target.\n") # Indicate the search is complete after finding the target