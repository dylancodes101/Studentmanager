import csv
from datetime import datetime

# Define the weight of each category as a percentage of the total grade
category_weights = {
    'Homework': 0.30,  # 30% of the total grade
    'Quiz': 0.20,      # 20% of the total grade
    'Exam': 0.50       # 50% of the total grade
}

# Initialize a dictionary to store the total points and earned points for each category
category_totals = {category: {'max_points': 0, 'earned_points': 0} for category in category_weights}
#print(category_totals)
# Read the grade book CSV file
with open('grades_student1.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    # Process each row in the CSV file
    for row in csv_reader:
        category = row['category']
        max_points = float(row['max_points'])
        earned_points = float(row['earned_points'])
        
        # Update the totals for the category
        category_totals[category]['max_points'] += max_points
        category_totals[category]['earned_points'] += earned_points

# Calculate the weighted average grade
weighted_average_grade = 0
for category, totals in category_totals.items():
    if totals['max_points'] > 0:  # Avoid division by zero
        category_percentage = totals['earned_points'] / totals['max_points']
        weighted_category_grade = category_percentage * category_weights[category]
        weighted_average_grade += weighted_category_grade

# Convert the weighted average grade to a percentage
weighted_average_grade *= 100

# Print the weighted average grade
print(f"Weighted Average Grade: {weighted_average_grade:.2f}%")

# Calculate the impact of each assignment on the overall grade
print("\nImpact of each assignment on the overall grade:")
with open('grades_student1.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        category = row['category']
        max_points = float(row['max_points'])
        earned_points = float(row['earned_points'])
        category_weight = category_weights[category]
        
        if category_totals[category]['max_points'] > 0:
            assignment_impact = (earned_points / max_points) * category_weight * 100
            print(f"{row['assignment_name']}: {assignment_impact:.2f}%")

