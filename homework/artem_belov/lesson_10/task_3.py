def decorator(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif second > first:
            return func(first, second, '/')
        elif first or second < 0:
            return func(first, second, '*')

    return wrapper


@decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    else:
        return first * second


first_user_input = int(input('Введи первое число: '))
second_user_input = int(input('Введи второе число: '))
result = calc(first_user_input, second_user_input)

print(round(result, 2))
