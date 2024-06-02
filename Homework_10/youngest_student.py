# Exercise 7: Find youngest student
# Write a function that takes a dictionary with information about students. Return info about the youngest student
# Dictionary example

students_info ={
    'student1':{
    'name': 'John Doe',
    'age' : 20,
    'subjects': ['Math',
    'Physics', 'English'],
    'scores': [17, 9, 9, 61],
    },
    'student2':{
    'name': 'Jane Smith',
    'age': 19,
    'subjects': ['Chemistry',
    'Biology', 'History'],
    'scores': [15, 6, 8, 101,]
    },
    'student3': {
    'name': 'Bob Johnson',
    'age': 21,
    'subjects': ['Computer Science', 'Statistics', 'Psychology'],
    'scores': [18, 8, 9, 9, 91,]
    }
}


def youngest_student(students_info):
    min_age = float('inf')
    youngest_student_info = None
    
    for student_id, info in students_info.items():
        if info['age'] < min_age:
            min_age = info['age']
            youngest_student_info = info
    
    return youngest_student_info

print(youngest_student(students_info))