# MV 1st Average Grade

cs_grade = int(input("What is your grade in cs: "))
math_grade = int(input("What is your grade in math: "))
seminary_grade = int(input("What is your grade in seminary: "))
advisory_grade = int(input("What is your grade in advisory: "))
english_grade = int(input("What is your grade in english: "))
art_grade = int(input("What is your grade in art: "))
biology_grade = int(input("What is your grade in biology: "))
                          
average = (cs_grade + math_grade + seminary_grade + advisory_grade + english_grade + art_grade + biology_grade)
average_grade = average/7
print(average_grade)

round(average_grade ,2)