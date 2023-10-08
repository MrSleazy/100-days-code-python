# Input a Python list of student heights
# student_heights = input().split()
student_heights = "180 124 165 173 189 169 146".split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

total_height = 0
num_students = 0

for height in student_heights:
    total_height += height
    num_students += 1

print(f"total height = {total_height}")
print(f"number of students = {num_students}")
print(f"average height = {round(total_height/num_students)}")
