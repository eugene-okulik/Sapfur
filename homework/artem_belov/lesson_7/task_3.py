def final_result(result):
    return int(result[result.index(":") + 2:]) + 10


print(final_result("результат операции: 42"))
print(final_result("результат операции: 54"))
print(final_result("результат работы программы: 209"))
print(final_result("результат: 2"))
