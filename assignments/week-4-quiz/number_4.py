# 4. Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
# percentage less than 50 (Grade C)
# percentage equal to 50 and less than 80 (Grade B)
# percentage equal to 80 and more than 80 (Grade A)

subjects = {
    "maths" : {},
    "english" : {},
    "physics" : {},
    "history" : {},
    "kiswahili" : {}
}

def grade_mark(mark):
    if mark < 50:
        return 'C'
    elif mark < 80:
        return 'B'
    else:
        return 'A'

def get_marks(subjects):
    for subject in subjects:
        try:
            mark = int(input(f"Enter the mark scored in {subject} : "))
            subjects[subject]["mark"] = mark
            subjects[subject]["grade"] = grade_mark(mark)
        except:
            print("Invalid input")

def get_total_average(subjects):
    total = 0
    average = 0
    for subject in subjects:
        total += subjects[subject]["mark"]
    average = total/5
    return total, average

def main():
    get_marks(subjects)
    total, average = get_total_average(subjects)
    print(f"Your total is {total} and your average is {average} %")
    print("Your grades are as follows:")
    for subject in subjects:
       print(subject, ":", subjects[subject]["grade"])

main()