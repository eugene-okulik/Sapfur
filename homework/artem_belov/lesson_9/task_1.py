import datetime

my_time = "Jan 15, 2023 - 12:05:33"

date = datetime.datetime.strptime(my_time, "%b %d, %Y - %H:%M:%S")

print(date.strftime("%B"))
print(date.strftime("%d.%m.%Y, %H:%M"))



