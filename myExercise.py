import sys
with open(sys.argv[1],"r") as file :
    student_list = file.read().splitlines()
    student_dict = {}
    for e in student_list :
        student = e.split(":")
        student_dict.update({student[0] : student[1]})    

for name in sys.argv[2].split(",") :
    try :
        print(f"Name: {name}, University: {student_dict[name]}")
    except :
        print(f"No record of '{name}' was found!")
        