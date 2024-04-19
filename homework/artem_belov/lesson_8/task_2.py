import sys

count = 0
sys.set_int_max_str_digits(50000)

def fibonacci_generator():
    a = 1
    b = 1
    while True:
        yield a
        a = b
        b = a + b


for num in fibonacci_generator():
    if count == 5:
        print(f'Пятое число:{num}')
    if count == 200:
        print(f'Двухсотое число:{num}')
    if count == 1000:
        print(f'Тысячное число:{num}')
    if count == 100000:
        print(f'Стотысячное число:{num}')
        break
    count += 1
