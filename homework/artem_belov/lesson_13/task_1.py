import os
import datetime

base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
task = os.path.join(base_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(task)


def read_file_task():
    with open(task, 'r') as data_file:
        for line in data_file.readlines():
            yield line


for task in read_file_task():
    date_list = task.split()
    date = (datetime.datetime.strptime(f'{date_list[1]} {date_list[2]}', '%Y-%m-%d %H:%M:%S.%f'))
    if task.startswith('1.'):
        date = date - datetime.timedelta(weeks=1)
    elif task.startswith('2.'):
        date = datetime.datetime.strftime(date, '%A')
    elif task.startswith('3.'):
        date_now = datetime.datetime.now()
        date = (date_now - date).days
    print(date)
