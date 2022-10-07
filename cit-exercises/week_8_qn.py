def answer_file(answers):
    f = open('answers.txt', 'w')
    for answer in answers:
        f.write(answer + '\n')
    f.close()

    f = open('answers.txt', 'r')
    answers = f.readlines()
    for answer in answers:
        print(answer)
    f.close()