# two hardcoded lists
list1 = ["Python", "JavaScript", "C++", "Ruby", "Go"]
list2 = ["JavaScript", "Python", "Rust", "Swift", "Go"]

# convert to sets
set1 = set(list1)
set2 = set(list2)

# set operations
print("Union:", set1 | set2)          # all languages, no duplicates
print("Intersection:", set1 & set2)   # languages in both lists
print("Difference:", set1 - set2)     # languages only in the first list
