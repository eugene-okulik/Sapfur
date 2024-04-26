def repeat_me(func):
    def wrapper(text, count):
        for _ in range(count):
            print(text)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', 2)


def repeat_me(count=2):
    def decorator(func):
        def wrapper(text):
            for _ in range(count):
                print(text)

        return wrapper

    return decorator


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
