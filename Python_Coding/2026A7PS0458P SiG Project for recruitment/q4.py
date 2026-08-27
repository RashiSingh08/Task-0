import numpy as np

students = np.array(["Alisha", "Dhara", "Ananya", "Kshama", "Sresht"])
marks = np.array([
    [72, 68, 85, 91, 54],  # Subject - Maths
    [65, 80, 95, 62, 78],  # Subject - English
    [70, 74, 80, 68, 88]   # Subject - Physics
])

row_x = marks[0]
print("Data type of Row 0:", row_x.dtype)

print(f"Mean Marks: {np.mean(marks):.2f}")
print(f"Max Mark: {np.max(marks)}")
print(f"Min Mark: {np.min(marks)}")
print(f"Standard Deviation: {np.std(marks):.2f}")

print("\nLast row before bonus:", marks[-1])
marks[-1] += 5
print("Last row after +5 bonus:", marks[-1])

bool_array = marks[-1] > 75
print("\nBoolean Array (Mask):")
print(bool_array)  

top_students = students[bool_array]
print("\nStudents scoring > 75 in the last row:")
print(top_students)