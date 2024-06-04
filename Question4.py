def get_unique_items(input_list):
    # Use a set to remove duplicates and then convert it back to a list
    unique_list = list(set(input_list))
    return unique_list

# Sample list
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]

# Get the unique list
unique_list = get_unique_items(sample_list)

# Print the unique list
print("Sample List:", sample_list)
print("Unique List:", unique_list)
