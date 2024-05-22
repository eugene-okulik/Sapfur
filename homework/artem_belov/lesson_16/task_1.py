import mysql.connector as mysql
import csv
import os
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

cursor = db.cursor(dictionary=True)


query = '''
SELECT *
FROM students
JOIN `groups` ON students.group_id = groups.id
JOIN books ON students.id = books.taken_by_student_id
JOIN marks ON students.id = marks.student_id
JOIN lessons on marks.lesson_id = lessons.id
JOIN subjets on lessons.subject_id = subjets.id
'''

cursor.execute(query)
data = cursor.fetchall()

with open(file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    next(file_data)
    for row in file_data:
        if row not in data:
            print(f"Информация не найдена: {row}")

db.close()
