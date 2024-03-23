# This assumes that student classes is an extant array with class objects that have the percent_grade method defined.
classes = {}
for class in student_classes:
    grade = class.percent_grade
    if grade>90:
        grade_point = 4
    elif grade>80:
        grade_point = 3
    elif grade>70:
        grade_point = 2
    elif grade>60:
        grade_point = 1
    else:
        grade_point = 0
    if class.weighted_ap == True && grade_point > 1:
        grade_point = grade_point + 10
    elif class.weighted_honors == grade_point > 1:
        grade_point = grade_point + 5
    classes.update(class, grade_point)
for k, v in classes:
    grade_point_total = grade_point_total + v
grade_point_average = grade_point_total/len(classes)
print(f"Your gpa is {grade_point_average}")
