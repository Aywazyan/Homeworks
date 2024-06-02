# Exercise 8: Find student with highest average score
# Write a function that takes a dictionary with information about students. Return info about the youngest student

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


def youngest_student_with_highest_score(students_info):
    youngest_age = float('inf')
    highest_average_score = float('-inf')
    youngest_student_info = None
    
    for student_id, info in students_info.items():
        average_score = sum(info['scores']) / len(info['scores'])
        if (info['age'] < youngest_age) or (info['age'] == youngest_age and average_score > highest_average_score):
            youngest_age = info['age']
            highest_average_score = average_score
            youngest_student_info = info

    return youngest_student_info
print(youngest_student_with_highest_score(students_info))