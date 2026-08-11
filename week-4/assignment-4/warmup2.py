student = {"name": "Ava","grade": "10th","subjects": ("Math", "Science", "History")}

# print each key-value pair
for key, value in student.items():
    print(key, ":", value)

# add new key
student["graduated"] = False

# print updated dictionary
print("\nUpdated dictionary:")
print(student)
