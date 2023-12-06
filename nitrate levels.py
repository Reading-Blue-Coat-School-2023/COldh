def calculate_dose(nitratelevel):
    # Check if the weight and age are within a certain range
    
    if nitratelevel > 10:
        return "for nitrate "
    elif weight >= 50 and age < 12:
        return "Medium dose"
    elif weight < 50 and age >= 12:
        return "High dose"
    else:
        return "Standard dose"

# Example usage:
weight = 60
age = 15
result = calculate_dose(weight, age)
print(f"For a weight of {weight} kg and age of {age} years, the recommended dose is: {result}")