#Write a Python program to insert space before every capital letter appears in a given word.
#Sample Data:
#("PythonExercises") -> "Python Exercises"
#("Python") -> "Python"
#("PythonExercisesPracticeSolution") -> "Python Exercises Practice Solution"
# QUESTION 6

def add_spaces(word):
    result = word[0]
    for ch in word[1:]:
        if ch.isupper():
            result += " "
        result += ch
    return result

print(add_spaces("PythonExercises"))               
print(add_spaces("Python"))                           
print(add_spaces("PythonExercisesPracticeSolution"))