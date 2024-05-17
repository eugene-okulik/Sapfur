import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO students (name, second_name) VALUES('Artem', 'Belov')")
student_id = cursor.lastrowid
print('student_id:', student_id)
db.commit()
insert_books = "INSERT INTO books(title, taken_by_student_id) VALUES(%s, %s)"
cursor.executemany(insert_books, [('HTML for new', student_id),
                                  ('CSS for new', student_id)])
db.commit()
cursor.execute("INSERT INTO `groups`(title, start_date, end_date) VALUES('group 900', 'Jan 1 2024', 'Sept 1 2024')")
group_id = cursor.lastrowid
print('group_id:', group_id)
db.commit()
cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")
db.commit()
cursor.execute("INSERT INTO subjets(title) VALUES('obj_1')")
subject_1 = cursor.lastrowid
db.commit()
cursor.execute("INSERT INTO subjets(title) VALUES('obj_2')")
subject_2 = cursor.lastrowid
db.commit()
insert_lesson = "INSERT INTO lessons(title, subject_id) VALUES(%s, %s)"
cursor.execute(insert_lesson, ('grid in css', subject_1))
lesson_1 = cursor.lastrowid
print('lesson_1:', lesson_1)
cursor.execute(insert_lesson, ('flexbox in css', subject_1))
lesson_2 = cursor.lastrowid
print('lesson_2:', lesson_2)
cursor.execute(insert_lesson, ('div in HTML', subject_2))
lesson_3 = cursor.lastrowid
print('lesson_3:', lesson_3)
cursor.execute(insert_lesson, ('position in HTML', subject_2))
lesson_4 = cursor.lastrowid
print('lesson_4:', lesson_4)
db.commit()
cursor.executemany(
    "INSERT INTO marks(`value`, lesson_id, student_id) VALUES(%s, %s, %s)",
    [('5', lesson_1, student_id), ('4', lesson_2, student_id),
     ('5', lesson_3, student_id), ('4', lesson_4, student_id)])
db.commit()
cursor.execute(f"SELECT * FROM marks WHERE student_id = {student_id}")
marks = cursor.fetchall()
print('marks:', marks)
cursor.execute(f"SELECT * FROM books WHERE taken_by_student_id = {student_id}")
books = cursor.fetchall()
print('books:', books)
all_for_student_query = f'''SELECT
s.`name`,
s.second_name,
g.title 'Группа',
b.title 'Книга',
sub.title 'Предмет',
l.title 'Урок',
m.`value` 'Оценка'
FROM
students s
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets sub ON l.subject_id = sub.id
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
WHERE s.id = {student_id}
'''
cursor.execute(all_for_student_query)
all_for_student_data = cursor.fetchall()
print('all_for_student_data:', all_for_student_data)
db.close()
