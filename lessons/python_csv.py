import csv

# csv.reader
# csv.writer

# my_csv = open('movies.csv', 'r')

# # data = csv.reader(my_csv, delimiter=',')
# data = csv.DictReader(my_csv, fieldnames = ['title', 'year', 'rating', 'metascore', 'votes', 'gross', 'runtime', 'genre', 'directors', 'actors', 'description'])

# # use the optional fieldnames parameter if you don't have headers in your data.
# # other optional parameters delimiter, quotechar, escapechar

# for row in data:
#     print(' '.join(list(row.values())), '\n')

# my_csv.close()

# with open('movies.csv', mode='r') as movies_csv:
#     data = csv.reader(movies_csv, delimiter=',')
#     for row in data:
#         print(row)

# writing to a file from a dictionary

# with open('employee_file2.csv', mode='w') as csv_file:
#     fieldnames = ['emp_name', 'dept', 'birth_month']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
#     writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})