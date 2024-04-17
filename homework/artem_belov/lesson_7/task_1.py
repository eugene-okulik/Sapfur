number = 10

while True:

    user_input = int(input('Введите цифру: '))
    if user_input == number:
        print('Угадал!')
        break
    else:
        print('Попробуйте снова')
