def student_averages(data):
    result = {}
    for student, grades in data.items():
        avg = sum(grades.values()) / len(grades)
        result[student] = round(avg)
    return result

def assignment_averages(data):
    result = {}
    
    for grades in data.values():
        for assignment in grades:
            result[assignment] = []

    for grades in data.values():
        for assignment, score in grades.items():
            result[assignment].append(score)

    for assignment in result:
        avg = sum(result[assignment]) / len(result[assignment])
        result[assignment] = round(avg)

    return result