def count_upper_lower(s):
    # Initialize counters
    upper_case_count = 0
    lower_case_count = 0
    
    # Iterate over each character in the string
    for char in s:
        if char.isupper():
            upper_case_count += 1
        elif char.islower():
            lower_case_count += 1
    
    # Print the results
    print(f"Numbrer of Upper-case characters: {upper_case_count}")
    print(f"Number of Lower-case Characters: {lower_case_count}")

# Input string
input_string = 'The quick Brow Fox'

# Call the function with the input string
count_upper_lower(input_string)
