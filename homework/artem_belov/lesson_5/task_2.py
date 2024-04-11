num_1 = "результат операции: 42"
num_2 = "результат операции: 514"
num_3 = "результат работы программы: 9"

result_1 = int(num_1[num_1.index(":") + 2:]) + 10
result_2 = int(num_2[num_2.index(":") + 2:]) + 10
result_3 = int(num_3[num_3.index(":") + 2:]) + 10

print(f'{result_1}, {result_2}, {result_3}')
