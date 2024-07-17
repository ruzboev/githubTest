reports = [
    (100000, "Income"),
    (120000, "Income"),
    (303000, "Outcome"),
    (110000, "Income")
]

# Create the dictionary from reports
new_dict = {}
for key, value in reports:
    if value not in new_dict:
        new_dict[value] = []
    new_dict[value].append(key)

print(new_dict)  # Print the created dictionary

# Define a function to add new income
def add_income(income):
    if "Income" in new_dict:
        new_dict["Income"].append(income)
    else:
        new_dict["Income"] = [income]

# New income to add
income_to_add = 5000  # Should be an integer, not a string
add_income(income_to_add)

print(new_dict)  # Print the dictionary after adding the new income